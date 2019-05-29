import requests
from helper import CMStudent

if __name__ == "__main__":
    student = CMStudent()
    student.signIn()

    base_dir = input('Output directory: ')

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