class CMAssessment:
    def __init__(self, assessment_id):
        self.assessment_id = assessment_id
        self.assessment_name = None
        self.points = None
        self.total_points = None
        self.mark_sent_out_date = None
        self.exam_pages_url = []
        self.num_of_pages = None
        self.exam_questions_points = []
        self.exam_master_questions_total_points = []
        