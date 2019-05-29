import requests
import os
import sys
import getpass
from PIL import Image, ImageDraw
from io import BytesIO
from tqdm import tqdm

class CMStudent:
    def __init__(self):
        self.session = requests.Session()
        self.cm_course_json = None

    def signIn(self):
        username = input('CM Email: ')
        password = getpass.getpass('CM Password: ')
        # password = input('CM Password: ')

        payload = {'user[email]': username, 'user[password]': password}
        cookies = self.session.post('https://app.crowdmark.com/sign-in', data=payload).cookies.get_dict()
        if 'cm_uuid' not in cookies:
            print("Login Failed. Incorrect email or password.", file=sys.stderr)
            sys.exit(1)
        
        print("Email and password have been verified.")
        print()

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
    
    def downloadAssessment(self, assessment_id, course_dir):
        url = 'https://app.crowdmark.com/api/v1/student/results/{}'.format(assessment_id)
        r = self.session.get(url)
        if r.status_code == 200:
            r_dict = r.json()
        else:
            print("showAllTestsAndAssignments Failed.", file=sys.stderr)
            sys.exit(1)

        jpeg_pages_url_list = []
        print("Title: {}".format(r_dict['included'][0]['attributes']['title']))
        for i in range(len(r_dict['included'])):
            if r_dict['included'][i]['type'] in ['exam-pages']:
                jpeg_page_link = r_dict['included'][i]['attributes']['url']
                jpeg_pages_url_list.append(jpeg_page_link)

        total_pages = len(jpeg_pages_url_list)
        im_list = []
        print("Downloading ... ")
        for i in tqdm(range(total_pages)):
            r = requests.get(jpeg_pages_url_list[i])
            if r.status_code == 200:
                im_list.append(Image.open(BytesIO(r.content)))
            # else:
                # print("ERROR")
                # if i != 0:
                #     new_img = Image.new('RGB', im_list[0].size, (255, 255, 255))
                #     ImageDraw.Draw(new_img).text((0, 0), 'Hello world!', (0, 0, 0))
                #     im_list.append(new_img)

        assert len(im_list) > 0
        out_pdf_filename = os.path.join(course_dir, r_dict['included'][0]['attributes']['title'])
        im_list[0].save(out_pdf_filename + ".pdf", "PDF", resolution=100.0, save_all=True, append_images=im_list[1:])
        print()
