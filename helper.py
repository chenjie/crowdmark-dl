import requests
import os
import sys
import getpass

class CMStudent:
    def __init__(self):
        self.session = requests.Session()
        self.cm_course_json = None

    def signIn(self):
        username = input('CM Email: ')
        password = getpass.getpass('CM Password:')

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
    
    def downloadAssessment(self, assessment_id, base_dir):
        url = 'https://app.crowdmark.com/api/v1/student/results/{}'.format(assessment_id)
        r = self.session.get(url)
        if r.status_code == 200:
            r_dict = r.json()
        else:
            print("showAllTestsAndAssignments Failed.", file=sys.stderr)
            sys.exit(1)

        out_dir = os.path.join(base_dir, r_dict['included'][0]['attributes']['title'])
        os.mkdir(out_dir)

        jpeg_pages_url_list = []
        print("Title: {}".format(r_dict['included'][0]['attributes']['title']))
        for i in range(len(r_dict['included'])):
            if r_dict['included'][i]['type'] in ['exam-pages']:
                jpeg_page_link = r_dict['included'][i]['attributes']['url']
                jpeg_pages_url_list.append(jpeg_page_link)

        total_pages = len(jpeg_pages_url_list)
        for i in range(total_pages):
            print("[{}/{}] Downloading ... ".format(i+1, total_pages), end = '')
            r = requests.get(jpeg_pages_url_list[i])
            if r.status_code == 200:
                print("OK")
                abs_filename = os.path.join(out_dir, "{}.jpeg".format(i+1))
            else:
                print("ERROR")
                abs_filename = os.path.join(out_dir, "{}.txt".format(i+1))
            with open(abs_filename, 'wb') as f:
                f.write(r.content)
        print()
