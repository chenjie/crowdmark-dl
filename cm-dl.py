import requests
from helper import CMStudent

# Get cookies
print("**The following id's are part of the cookies, which is used for authentication purpose only.**")
# cm_session_id = input('cm_session_id: ')
# cm_uuid = input('cm_uuid: ')
# base_dir = input('Output directory: ')

print()

# =======================================
cm_session_id = '6b18da7a52613d17836d0e16328e2293'
cm_uuid = 'be3d294b-fade-4a4e-85c6-c67d5c3fda8f'
base_dir = '/Users/jackni/Desktop/19sum/cm-dl-test'
# cm_course_url = 'https://app.crowdmark.com/student/courses/fall-2015-mat137y1-y-tut0202-tut0201-tut5103-tut5'
# =======================================

# cm_course_url_arr = cm_course_url.split('/')
# if not cm_course_url_arr[-1]:
#     course_name = cm_course_url_arr[-2]
# else:
#     course_name = cm_course_url_arr[-1]

# print("course_name is " + course_name)


student = CMStudent(cm_session_id, cm_uuid)
student.getAllCourses()

while 1:
    student.showAllCourses()

    print()

    course_name = student.getCourseNameFromStdin()
    assessment_id_list = student.showAllTestsAndAssignments(course_name)

    # idx_selected = 3
    # assessment_id_list = student.showAllTestsAndAssignments(r_dict['data'][idx_selected]['id'])

    print()

    idx_selected = int(input("Please enter an index to select an assessment: "))
    if idx_selected == len(assessment_id_list):
        # download all assessments
        for i in assessment_id_list:
            student.downloadAssessment(i, base_dir)
    else:
        student.downloadAssessment(assessment_id_list[idx_selected], base_dir)