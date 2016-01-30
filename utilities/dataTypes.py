class Course:
    def __init__(self, subject="", number="", title="", units="", prereqs="", concurrent="", coreqs=""):
        self.subject = subject
        self.number = number
        self.title = title
        self.units = units
        self.prereqs = prereqs
        self.concurrent = concurrent
        self.coreqs = coreqs
        pass

class CourseTuple:
    def __init__(self, num="", courses = [], coursetuples = []):
        self.num = num
        self.courses = courses
        self.coursetuples = coursetuples
