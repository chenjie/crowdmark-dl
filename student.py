import os
import sys
import getpass
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm
import arrow
from assessment import CMAssessment


class CMStudent:
    def __init__(self):
        self.session = requests.Session()
        self.cm_course_json = None

    def signIn(self):
        fail_times = 0
        while fail_times < 3:
            tmp = input('CM Email: ')
            if (fail_times == 0) or tmp:
                username = tmp
            password = getpass.getpass('CM Password: ')

            payload = {'user[email]': username, 'user[password]': password}
            cookies = self.session.post('https://app.crowdmark.com/sign-in', data=payload).cookies.get_dict()
            if 'cm_uuid' not in cookies:
                print("✘ Incorrect email or password. Please try again. ✘", file=sys.stderr)
                print("You can press enter to keep the precious CM Email.", file=sys.stderr)
                fail_times += 1
            else:
                print("✔ Email and password have been verified.")
                print()
                return
        print("Login failed. Bye.", file=sys.stderr)
        sys.exit(1)

    def getAllCourses(self):
        payload = {'all': 'true', 'filter[is_student]': 'true'}
        url = 'https://app.crowdmark.com/api/v2/courses'
        r = self.session.get(url, params=payload)
        if r.status_code == 200:
            self.cm_course_json = r.json()
        else:
            print("getAllCourses Failed.", file=sys.stderr)
            sys.exit(1)
        
    def showAllCourses(self):
        print("All the courses records on Crowdmark:")
        for i in range(len(self.cm_course_json['data'])):
            print("[{}] {}".format(i, self.cm_course_json['data'][i]['id']))

    def getCourseNameFromStdin(self):
        d = input("Please enter an index to select a course (type 'q' to quit): ")
        if d == 'q':
            print("Bye.")
            sys.exit()
        idx_selected = int(d)
        return self.cm_course_json['data'][idx_selected]['id']

    def showAllTestsAndAssignments(self, course_name):
        payload = {'filter[course]': course_name}
        url = 'https://app.crowdmark.com/api/v2/student/assignments'
        r = self.session.get(url, params=payload)
        if r.status_code == 200:
            r_dict = r.json()
        else:
            print("showAllTestsAndAssignments Failed.", file=sys.stderr)
            sys.exit(1)

        assessment_id_list = []
        print("All tests & assignments of the course {}:".format(course_name))
        i = 0
        while i < len(r_dict['data']):
            assessment_id_list.append(r_dict['data'][i]['id'])
            print("[{}] {}".format(i, r_dict['data'][i]['relationships']['exam-master']['data']['id']))
            i += 1
        print("[{}] all".format(i))

        return assessment_id_list
    
    def getAssessmentMetadata(self, assessment_id):
        url = 'https://app.crowdmark.com/api/v1/student/results/{}'.format(assessment_id)
        r = self.session.get(url)
        if r.status_code == 200:
            r_dict = r.json()
        else:
            print("showAllTestsAndAssignments Failed.", file=sys.stderr)
            sys.exit(1)

        cma = CMAssessment(assessment_id)
        cma.assessment_name = r_dict['included'][0]['attributes']['title']
        cma.points = int(float(r_dict['data']['attributes']['total']))
        cma.total_points = int(float(r_dict['included'][0]['attributes']['total-points']))
        cma.mark_sent_out_date = arrow.get(r_dict['included'][0]['attributes']['marks-sent-at'])

        print("Title: {}".format(cma.assessment_name))
        for i in range(len(r_dict['included'])):
            cm_entry = r_dict['included'][i]
            cm_type = cm_entry['type']
            if cm_type == 'exam-pages':
                cma.exam_pages_url.append(cm_entry['attributes']['url'])
            elif cm_type == 'exam-master-questions':
                cma.exam_master_questions_total_points.append(cm_entry['attributes']['points'])
            elif cm_type == 'exam-questions':
                cma.exam_questions_points.append(cm_entry['attributes']['points'])
        
        assert len(cma.exam_questions_points) == len(cma.exam_master_questions_total_points)
        cma.num_of_pages = len(cma.exam_questions_points)

        return cma
    
    def downloadAssessment(self, cma, course_dir):
        # PIL image related config
        im_list = []
        font = ImageFont.truetype("google-fonts/OpenSans-Regular.ttf", 20)

        num_of_entries = len(cma.exam_pages_url)
        cur_page = 0
        print("Downloading ... ")
        # tqdm progress bar :)
        with tqdm(total=cma.num_of_pages) as pbar:
            for i in range(num_of_entries):
                r = requests.get(cma.exam_pages_url[i])
                if r.status_code != 200:
                    continue

                cursor_pos = 0
                pil_img = Image.open(BytesIO(r.content))
                if not im_list:
                    # First page
                    ImageDraw.Draw(pil_img).text((0, 0), 
                        'Title: {}'.format(cma.assessment_name), (0, 0, 255), font=font)
                    ImageDraw.Draw(pil_img).text((0, 25), 
                        'Marks Sent At: {}'.format(cma.mark_sent_out_date.to('local').format(
                            'YYYY-MM-DD dddd HH:mm:ss ZZZ')), (0, 0, 255), font=font)
                    ImageDraw.Draw(pil_img).text((0, 50), 
                        'Total Score: {}% ({}/{})'.format(int(cma.points/cma.total_points * 100), 
                        cma.points, cma.total_points), (0, 0, 255), font=font)
                    cursor_pos += 75

                if cma.exam_questions_points[cur_page] == 'null':
                    ImageDraw.Draw(pil_img).text((0, cursor_pos), 
                        'Not graded.', (255, 0, 0), font=font)
                else:
                    ImageDraw.Draw(pil_img).text((0, cursor_pos), 
                        'Score: {}/{}'.format(cma.exam_questions_points[cur_page], 
                        cma.exam_master_questions_total_points[cur_page]), (255, 0, 0), font=font)
                im_list.append(pil_img)
                cur_page += 1
                pbar.update(1)

        assert len(im_list) > 0
        out_pdf_filename = os.path.join(course_dir, cma.assessment_name)
        im_list[0].save(out_pdf_filename + ".pdf", "PDF", resolution=100.0, save_all=True, append_images=im_list[1:])
        print()
