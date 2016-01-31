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
class CourseTuple:
    def __init__(self, numRequired = 0, courses = [], courseTuples = []):
        self.numRequired = numRequired
        self.courses = courses
        self.courseTuples = courseTuples

class Course:
    def __init__(self, subject = "", number = "", title = "", units = 0, prereqs = CourseTuple(), concurrent = CourseTuple(), coreqs = CourseTuple(), seasonsOffered = {"fall": False, "winter": False, "spring": False}):
        self.subject = subject
        self.number = number
        self.title = title
        self.units = units
        self.prereqs = prereqs
        self.concurrent = concurrent
        self.coreqs = coreqs
        self.seasonsOffered = seasonsOffered # default to false

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
    # @param completed is an array of completed courses (or equivalent)
    def __init__(self, quarters = [], completed = []):
        assert all(isinstance(quarter, Quarter) for quarter in quarters)
        self.quarters = quarters
    # get # of filled quarters
    def getNumQuarters(self):
        return len(self.quarters)
    def isCompleted(self, course):
        for completedCourse in completed:
            completedId = completedCourse.subject + completedCourse.number
            courseId = course.subject + course.number
            if completedId == courseId:
                return True
        return False




########################
# Function definitions
########################

# used for checking pre-reqs AND co-reqs
# return true if course is in plan, checking up until quarter [endIndex]
# @param offset is the number of quarters from the end of the plan at which it stops searching
def courseInPlan(course, plan, offset):
    # inspect every quarter in plan
    for i in range(0, len(plan.quarters)-offset):
        # inspect every course in quarter
        for prevCourse in plan.quarters[i].courses:
            idPrevCourse = prevCourse.subject + prevCourse.number
            idCourse = course.subject + course.number
            if idPrevCourse == idCourse:
                return True
    return False

# return true if the course tuple is satisfied, given the current plan and offset (quarters from the current quarter to cut the check sort)
def satisfied(plan, courseTuple, offset):
    if courseTuple.numRequired == 0:
        return True
    numSatisfied = 0
    for course in courseTuple.courses:
        if plan.isCompleted(course) or courseInPlan(course, plan, offset):
            numSatisfied += 1
        if numSatisfied >= courseTuple.numRequired:
            return True
    for nestedTuple in courseTuple.tuples:
        if satisfied(plan, nestedTuple, offset):
            numSatisfied += 1
        if numSatisfied >= courseTuple.numRequired:
            return True
    return False

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

    # 1. course already placed in plan?
    if courseInPlan(newCourse, currentPlan, 0):
        print("New course has already been placed.")
        return False

    # 2. is it offered this quarter?
    currentSeason = currentPlan.quarters[currentQuarter].season
    if not newCourse.seasonsOffered[currentSeason]:
        print("New course is not offered this quarter.")
        return False

    # 3. All pre-reqs satisfied? 
    # @param offset=1 b/c checking pre-reqs so must be 1 qtr back
    if not satisfied(newCourse.preReqs, 1, currentPlan):
        return False

    # At very end if none of the conditions fail
    return True

    
    


########################
# Main
########################
def main():
    # init/create data structures
    # prev taken coursework
    completedCourses = [Course("MATH", "21"), Course("CMPE", "16")];
    courses = [
            [Course("AMS", "10", "Applied Bullshit", 5), Course("PHYS", "5A", "Intro to Cuntimatics", 5), Course("PHYS", "5L", "Intro to Cuntimatics, Lab", 1)], 
            [Course("AMS", "20", "Applied Bullshit", 5), Course("PHYS", "5B", "Intro to Cuntimatics", 5), Course("PHYS", "5M", "Intro to Cuntimatics, Lab", 2)]
            ]
    quarters = [Quarter(courses[0], "fall"), Quarter(courses[1], "winter"), Quarter([], "spring")]
    plan = CoursePlan(quarters, completedCourses)

    pCourses = [Course("CMPE", "16")];
    # preReq tuple
    p5c = CourseTuple(3, [Course("CMPE", "16"), courses[0][0]], [CourseTuple(1, [courses[0][1], courses[][]], []), CourseTuple()])

    # print plan
    printCoursePlan(plan);

    # define course for testing
    newCourse = Course("PHYS", "5C", "Intro to Cuntimatics", 5, [], [], [], {"fall":False, "winter":True, "spring":True})

    # courseEval unit test 
    if courseEval(newCourse, plan, 19, 2):
        print("Course eval succeeded.")
    else:
        print("Course eval failed.")




main()
