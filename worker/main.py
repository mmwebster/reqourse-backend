# import data types
# from ..utilities import dataTypes

class Course:
    def __init__(self, subject = "", number = 0, title = "", units = 0, prereqs = [], concurrent = [], coreqs = []):
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

class PlanQuarter:
    def __init__(self, courses = []);
        self.courses = courses;

class CoursePlan:
    def __init__(self, quarters = []);
        assert type(quarters) 
        self.quarters = quarters;



print("Hello");

x = Course("AMS", 10, "Applied Bullshit", 5);
y = PlanQuarter([x]);
z = CoursePlan([y]);

# def printCoursePlan(

# courselist = []
# tuplelist = []

# Evaluation of an individual course, for whether or not it passes the constraints
def courseEval(course, currentPlan, maxUnits):
    assert type(course) == Course
    assert type(currentPlan) == CoursePlan
    assert type(maxUnits) == int
