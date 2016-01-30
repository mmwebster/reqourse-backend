# import data types
# from ..utilities import dataTypes

class Course:
    def __init__(self, subject = "", number = "", title = "", units = 0, prereqs = [], concurrent = [], coreqs = []):
        self.subject = subject
        self.number = number
        self.title = title
        self.units = units
        self.prereqs = prereqs
        self.concurrent = concurrent
        self.coreqs = coreqs
        pass

class CourseTuple:
    def __init__(self, num = 0, courses = [], coursetuples = []):
        self.num = num
        self.courses = courses
        self.coursetuples = coursetuples

class Quarter:
    def __init__(self, courses = [], units = 0):
        self.courses = courses
        self.units = units

class CoursePlan:
    def __init__(self, quarters = []):
        assert type(quarters) 
        self.quarters = quarters

def printCoursePlan(plan):
    assert type(plan) == CoursePlan
    print("correct type")
    print("Plan:")
    for quarter in plan.quarters:
        print(" (" + str(quarter.units) + "un)")
        # for course in quarter.courses
        #     print("-" + course.subject + str(course.number))
        print("\n")

            
    
    

# courselist = []
# tuplelist = []

# Evaluation of an individual course, for whether or not it passes the constraints
def courseEval(course, currentPlan, maxUnits):
    assert type(course) == Course
    assert type(currentPlan) == CoursePlan
    assert type(maxUnits) == int

def main():
    # init courses and create them
    courses = [Course("AMS", "10", "Applied Bullshit", 5), Course("PHYS", "5A", "Intro to Cuntimatics", 5), Course("PHYS", "5L", "Intro to Cuntimatics, Lab", 1)]
    # init quarter
    quarter = Quarter()
    # add all courses to quarter
    for course in courses:
        print("Course is " + course.title);
    # for i in range(len(courses)):
    #     quarter.courses[i] = courses[i];
    # init overall plan
    plan = CoursePlan([quarter])
    # print plan
    printCoursePlan(plan);

main()
