import requests
import os
from student import CMStudent
from utils import getBaseDir, getCourseDir


if __name__ == "__main__":
    student = CMStudent()
    student.signIn()
    base_dir = getBaseDir()
    student.getAllCourses()
    while 1:
        course_list = student.showAllCourses()
        course_ipt = student.getCourseNameFromStdin()
        if course_ipt != 'a':
            course_list = [course_ipt]
        for course_name in course_list:
            course_dir = getCourseDir(base_dir, course_name)
            assessment_id_list = student.showAllTestsAndAssignments(course_name)
            if course_ipt == 'a':
                for assessment_id in assessment_id_list:
                    student.downloadAssessment(assessment_id, course_dir)
            else:
                idx_selected = int(input("Please enter an index to select an assessment: "))
                if idx_selected == len(assessment_id_list):
                    for assessment_id in assessment_id_list:
                        student.downloadAssessment(assessment_id, course_dir)
                else:
                    student.downloadAssessment(assessment_id_list[idx_selected], course_dir)
        if course_ipt == 'a':
            print("All tasks completed! Bye.")
            break
