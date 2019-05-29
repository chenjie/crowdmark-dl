import requests
from helper import CMStudent

# Get cookies
print()
print("**The following id's are part of the cookies, which is used for authentication purpose only.**")
cm_session_id = input('cm_session_id: ')
cm_uuid = input('cm_uuid: ')
base_dir = input('Output directory: ')

print()

student = CMStudent(cm_session_id, cm_uuid)
student.getAllCourses()

while 1:
    student.showAllCourses()

    print()

    course_name = student.getCourseNameFromStdin()
    assessment_id_list = student.showAllTestsAndAssignments(course_name)

    print()

    idx_selected = int(input("Please enter an index to select an assessment: "))
    if idx_selected == len(assessment_id_list):
        for ass in assessment_id_list:
            student.downloadAssessment(ass, base_dir)
    else:
        student.downloadAssessment(assessment_id_list[idx_selected], base_dir)