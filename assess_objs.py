class CMAssessment:
    def __init__(self, assessment_id):
        self.course_name = None
        self.assessment_id = assessment_id
        self.assessment_id_v2 = None
        self.assessment_name = None
        self.instructor = None
        self.points = None
        self.total_points = None
        self.mark_sent_out_date = None
        self.id2Q_dict = {}

        # backward compatability
        self.exam_pages_url = []
        self.exam_questions_points = []
        self.exam_master_questions_total_points = []
    
    def setInstructor(self, instructor):
        self.instructor = instructor
    
    def setCourseName(self, course_name):
        self.course_name = course_name
    
    def setAssessmentIdV2(self, assessment_id_v2):
        self.assessment_id_v2 = assessment_id_v2
    
    def setAssessmentName(self, assessment_name):
        self.assessment_name = assessment_name

    def setScoreAndTotalPoints(self, points, total_points):
        self.points = points
        self.total_points = total_points

    def setDate(self, mark_sent_out_date):
        self.mark_sent_out_date = mark_sent_out_date
    
    def addQ(self, QID, Q):
        self.id2Q_dict[QID] = Q


class CMQuestion:
    def __init__(self, QID):
        self.QID = QID
        self.pid2pageInfo_dict = {}
        self.points = None
        self.total_points = None
        self.seq = None
        self.approximate_num_pages = 0
        self.found_page_urls = False
    
    def addPage(self, page_id, url):
        self.pid2pageInfo_dict[page_id] = {'url': url, 'seq_approx': self.approximate_num_pages}
        self.approximate_num_pages += 1

    def setPoints(self, points):
        self.points = points
    
    def setTotalPoints(self, total_points):
        self.total_points = total_points
    
    def setSeq(self, seq):
        self.seq = seq


class CMInstructor:
    def __init__(self, name, email):
        self.name = name
        self.email = email