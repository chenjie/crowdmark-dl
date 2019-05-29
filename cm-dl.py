import requests
from helper import CMStudent
import os

if __name__ == "__main__":
    student = CMStudent()
    student.signIn()

    base_dir = input('Output directory: ')
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)

    student.getAllCourses()

    while 1:
        student.showAllCourses()

        print()

        course_name = student.getCourseNameFromStdin()
        course_dir = os.path.join(base_dir, course_name)
        if not os.path.exists(course_dir):
            os.mkdir(course_dir)
        assessment_id_list = student.showAllTestsAndAssignments(course_name)

        print()

        idx_selected = int(input("Please enter an index to select an assessment: "))
        if idx_selected == len(assessment_id_list):
            for ass in assessment_id_list:
                student.downloadAssessment(ass, course_dir)
        else:
            student.downloadAssessment(assessment_id_list[idx_selected], course_dir)