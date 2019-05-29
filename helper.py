import requests
import os
import sys

class CMStudent:
    def __init__(self, cm_session_id, cm_uuid):
        self.cm_session_id = cm_session_id
        self.cm_uuid = cm_uuid
        self.cm_course_json = None

    def getAllCourses(self):
        payload = {'all': 'true', 'filter[is_student]': 'true'}
        url = 'https://app.crowdmark.com/api/v2/courses'
        cookies = {'cm_session_id': self.cm_session_id, 'cm_uuid': self.cm_uuid}
        self.cm_course_json = requests.get(url, params=payload, cookies=cookies).json()

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
        cookies = {'cm_session_id': self.cm_session_id, 'cm_uuid': self.cm_uuid}
        r_dict = requests.get(url, params=payload, cookies=cookies).json()

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
        cookies = {'cm_session_id': self.cm_session_id, 'cm_uuid': self.cm_uuid}
        r_dict = requests.get(url, cookies=cookies).json()

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
