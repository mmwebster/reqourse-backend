# import data types
# from ..utilities import dataTypes


########################
# Class definitions
########################
class Course:
    def __init__(self, subject = "", number = "", title = "", units = 0, prereqs = [], concurrent = [], coreqs = []):
        self.subject = subject
        self.number = number
        self.title = title
        self.units = units
        self.prereqs = prereqs
        self.concurrent = concurrent
        self.coreqs = coreqs

class CourseTuple:
    def __init__(self, num = 0, courses = [], coursetuples = []):
        self.num = num
        self.courses = courses
        self.coursetuples = coursetuples

class Quarter:
    def __init__(self, courses = []):
        self.courses = courses
    # get total num of units in quarter
    def getUnits(self):
        n = 0
        for course in self.courses:
            print("---> is " + course.title)
            n += course.units
        return n
            
class CoursePlan:
    def __init__(self, quarters = []):
        assert all(isinstance(quarter, Quarter) for quarter in quarters)
        self.quarters = quarters




########################
# Function definitions
########################

# print out a single course plan
def printCoursePlan(plan):
    assert isinstance(plan, CoursePlan)
    print("Plan:")
    for quarter in plan.quarters:
        print(" (" + str(quarter.getUnits()) + "un)")
        for course in quarter.courses:
            print("-" + course.subject + str(course.number))
        print("\n")

# Evaluation of an individual course, for whether or not it passes the constraints
def courseEval(course, currentPlan, maxUnits):
    assert type(course) == Course
    assert type(currentPlan) == CoursePlan
    assert type(maxUnits) == int




########################
# Main
########################
def main():
    # init courses and create them
    courses = [Course("AMS", "10", "Applied Bullshit", 5), Course("PHYS", "5A", "Intro to Cuntimatics", 5), Course("PHYS", "5L", "Intro to Cuntimatics, Lab", 1)]
    # init quarter
    quarter = Quarter()
    # add all courses to quarter
    for course in courses:
        print("Course is " + course.subject + course.number);
        quarter.courses.append(course) # = courses[i];

    # for i in range(len(courses)):
    # init overall plan
    plan = CoursePlan([quarter])
    # print plan
    printCoursePlan(plan);

main()
