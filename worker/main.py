# import data types
# from ..utilities import dataTypes
# from enum import Enum

########################
# Enum definitions
########################
# class Season(Enum):
#     fall = False
#     winter = False
#     spring = False


########################
# Class definitions
########################
class Course:
    def __init__(self, subject = "", number = "", title = "", units = 0, prereqs = [], concurrent = [], coreqs = [], seasonsOffered = {"fall": False, "winter": False, "spring": False}):
        self.subject = subject
        self.number = number
        self.title = title
        self.units = units
        self.prereqs = prereqs
        self.concurrent = concurrent
        self.coreqs = coreqs
        self.seasonsOffered = seasonsOffered # default to false

class CourseTuple:
    def __init__(self, numRequired = 0, courses = [], coursetuples = []):
        self.numRequired = numRequired
        self.courses = courses
        self.coursetuples = coursetuples

class Quarter:
    def __init__(self, courses = [], season = ""):
        self.courses = courses
        self.season = season
    # get total num of units in quarter
    def getUnits(self):
        n = 0
        for course in self.courses:
            n += course.units
        return n
            
class CoursePlan:
    def __init__(self, quarters = []):
        assert all(isinstance(quarter, Quarter) for quarter in quarters)
        self.quarters = quarters
    # get # of filled quarters
    def getNumQuarters(self):
        return len(self.quarters)




########################
# Function definitions
########################

# print out a single course plan
def printCoursePlan(plan):
    assert isinstance(plan, CoursePlan)
    print("Plan:")
    for i in range(len(plan.quarters)):
        print(" Qtr " + str(i + 1) + ", " + str(plan.quarters[i].getUnits()) + " unit(s)")
        for course in plan.quarters[i].courses:
            print(" -" + course.subject + str(course.number))

# Evaluation of an individual course, for whether or not it passes the constraints
def courseEval(newCourse, currentPlan, maxUnits, currentQuarter):
    # confirm correct type
    assert isinstance(newCourse, Course)
    assert isinstance(currentPlan, CoursePlan)
    assert type(maxUnits) == int
    assert type(currentQuarter) == int

    # course already placed in plan?
    # inspect every quarter in plan
    for quarter in currentPlan.quarters:
        # inspect every course in quarter
        for course in quarter.courses:
            idPrevCourse = course.subject + course.number
            idNewCourse = newCourse.subject + newCourse.number
            if idPrevCourse == idNewCourse:
                return False

    currentSeason = currentPlan.quarters[currentQuarter].season
    if not newCourse.seasonsOffered[currentSeason]:
        return False


    # At very end if none of the conditions fail
    return True

    
    


########################
# Main
########################
def main():
    # init/create data structures
    courses = [
            [Course("AMS", "10", "Applied Bullshit", 5), Course("PHYS", "5A", "Intro to Cuntimatics", 5), Course("PHYS", "5L", "Intro to Cuntimatics, Lab", 1)], 
            [Course("AMS", "20", "Applied Bullshit", 5), Course("PHYS", "5B", "Intro to Cuntimatics", 5), Course("PHYS", "5M", "Intro to Cuntimatics, Lab", 2)]
            ]
    quarters = [Quarter(courses[0], "fall"), Quarter(courses[1], "winter")]
    plan = CoursePlan(quarters)

    # print plan
    printCoursePlan(plan);

    # define course for testing
    newCourse = Course("PHYS", "5C", "Intro to Cuntimatics", 5, [], [], [], {"fall":False, "winter":True, "spring":True})

    # courseEval unit test 
    if courseEval(newCourse, plan, 19, 1):
        print("Course eval succeeded.")
    else:
        print("Course eval failed.")




main()
