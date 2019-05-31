import os


def getBaseDir():
    base_dir = input('Output directory: ')
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    return base_dir

def getCourseDir(base_dir, course_name):
    course_dir = os.path.join(base_dir, course_name)
    if not os.path.exists(course_dir):
        os.mkdir(course_dir)
    return course_dir