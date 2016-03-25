#####################################################################################
# GENERAL NOTES
#####################################################################################
# 1. Course tuples were removed and now referred to as nodes (but aren't entirely the same)
# 2. Style guidelines: For every new section, enclose the same hash formation as seen elsewhere, for every new class or function definition enclose with the same asterisks seen elsewhere. The end of a section should be followed by three new lines, while the everywhere else different component should be delimited a single new line.



#####################################################################################
# Enum definitions
#####################################################################################

# ***********************************************************************************
# @desc currently not being used, was previously not syntactically correct. Can probably reference
#       by just Seasons.fall, etc.
# ***********************************************************************************
class Seasons:
    fall = False
    winter = False
    spring = False

# ***********************************************************************************
# @desc The type of relationship between a node and its parent (only one parent)
# ***********************************************************************************
class ParentRel:
    pre = False
    co = False
    concurrent = False # not taking into account in most situations



#####################################################################################
# Class definitions
#####################################################################################

# ***********************************************************************************
# @desc A basic queue implementation
# ***********************************************************************************
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item) # pushes new element to "end" of queue
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

# ***********************************************************************************
# @desc A node in one of the course-dependent trees; acts like a container for courses that may or
#       may not be filled.
# @param children All child nodes
# @param numRequired The number of the children that must be satisfied in the tree to take this course
# @param course A single course definition (optional) for this node
# @param parentRel The type of relationship between the course in this node and that in its parent.
#        Must be dict. [rel. type]->[boolean]. (optional..not used if does not contain course)
# ***********************************************************************************
class Node:
    def __init__(self, children = [], numRequired = 0, course = None, parentRel = {}):
        self.children = children
        self.numRequired = numRequired
        self.course = course
        self.parentRel = parentRel

# ***********************************************************************************
# @desc A single course and its attributes
# @param subject The subject code (string) used to catagorize the course by
# @param number The number used to uniquely identify a course within a subject
# @param title The name of the course as it is displayed and used
# @param seasonsOffered A dictionary with [season name]->[boolean] pairs...when the course is offered
# ***********************************************************************************
class Course:
    def __init__(self, subject, number, title, units, seasonsOffered = {}):
        self.subject = subject
        self.number = number
        self.title = title
        self.units = units
        self.seasonsOffered = seasonsOffered

# ***********************************************************************************
# @desc A single quarter in the Timeline
# @param courses An array of courses inserted into the specific quarter
# @param season A string containing the season this quarter is in..used with course season dict.
# @param maxUnits the max number of units desired for this quarter
# ***********************************************************************************
class Quarter:
    def __init__(self, courses = [], season = None, maxUnits = 20):
        assert all(isinstance(course, Course) for course in courses)
        self.courses = courses
        self.season = season
        self.maxUnits = maxUnits
    # @desc Returns the total number of units currently stored in this quarter
    def getUnits(self):
        totalUnits = 0
        for course in self.courses:
            totalUnits += course.units
        return totalUnits

# ***********************************************************************************
# @desc The planned out courses in their quarter with respect their seasons
# @param quarters Contains of the currently planned out quarters
# @param completedCourses Contains a bucket (dictionary) of all completed courses in the format
#        [cid]->[course]
# @param currentQuarter Index of the quarter the user is currently in..this might be unecessary
# ***********************************************************************************
class Timeline:
    def __init__(self, quarters = [], completedCourses = {}, currentQuarter = 0):
        assert all(isinstance(quarter, Quarter) for quarter in quarters)
        self.quarters = quarters
        self.completed = completedCourses
        self.currentQuarter = currentQuarter
    # @desc Return the # of populated quarters
    def getNumQuarters(self):
        return len(self.quarters)
    # @desc Returns a boolean of whether or not the passed quarter has been completed
    # @param course The course to test for having been completed
    def isCompleted(self, course):
        cid = course.subject + str(course.number)
        if cid in self.completedCourses:
            return True
        else:
            return False



#####################################################################################
# Function definitions
#####################################################################################

# ***********************************************************************************
# @desc Used for ensuring that a courses pre-reqs and co-reqs have been satisfied during individual course eval
# @param course The course to search for that must be satisfied
# @param timeline A reference to the currently planned out timeline
# @param reqType The type of requirement.."pre" or "co"
# ***********************************************************************************
def courseSatisfied(course, timeline, reqType):
    cid = course.subject + str(course.number)
    # first check completedCourses in timeline
    if cid in timeline.completedCourses:
        return True
    else:
        # now check the previous quarter based on reqType
        offset = 1 if reqType == "pre" else 0
        # inspect every quarter in plan
        for i in range(0, len(timeline.quarters)-offset):
            # inspect every course in quarter
            for prevCourse in timeline.quarters[i].courses:
                prevCid = prevCourse.subject + str(prevCourse.number)
                if prevCid == cid:
                    return True
    return False

# ***********************************************************************************
# @desc Prints out every quarter in the timeline and every course within every quarter
# @param timeline The timeline to print out
# ***********************************************************************************
def printTimeline(timeline):
    assert isinstance(timeline, Timeline)
    print("Timeline:")
    for i in range(len(timeline.quarters)):
        print(" Qtr " + str(i + 1) + ", " + str(timeline.quarters[i].getUnits()) + " units(s), (" + timeline.quarters[i].season + ")")
        for course in timeline.quarters[i].courses:
            print(" -" + course.subject + str(course.number))

# ***********************************************************************************
# @desc Basic BFS implementation
# ***********************************************************************************
# def bfs(node):
#     assert isinstance(node, Node)
#     queue = Queue()
#     queue.enqueue(node)
#
#     # proceed with BFS, printing element along the way
#     while not queue.isEmpty():
#         n = queue.dequeue()
#         # !!!
#         # DO SOMETHING W/ DATA
#         # !!!
#         # queue every child of n
#         for child in n.children:
#             queue.enqueue(child)

# ***********************************************************************************
# @desc Prints out a tree given the head node. Uses a BFS type implementation w/ mods.
# @param head The head of the tree, of type Node
# ***********************************************************************************
def printTree(head):
    currentLevel = [head]
    while currentLevel:
        nextLevel = []
        for node in currentLevel:
            if not node.course == None:
                print "(numReq: " + str(node.numRequired) + ", cid: " + node.course.subject + str(node.course.number) + ")",
            else:
                print "(numReq: " + str(node.numRequired) + ", cid: )",

            for child in node.children:
                nextLevel.append(child)
        print # add new line
        currentLevel = nextLevel # proceed to next level



#####################################################################################
# Main
#####################################################################################
def main():
    # create testing data
    # completedCourses = {"MATH21": Course("MATH", "21", None, 5)};
    # courses = [ \
    #         Course("AMS", "10", None, 5, {"fall":True, "winter":True, "spring":False}), \
    #         Course("PHYS", "5A", None, 5), \
    #         Course("PHYS", "5L", None, 1), \
    #         Course("AMS", "20", None, 5), \
    #         Course("PHYS", "5B", None, 5), \
    #         Course("PHYS", "5M", None, 1) \
    #         ]
    completedCourses = {}
    courses = {
            "c4": Course("C", "4", None, 5),
            "c5": Course("C", "5", None, 5),
            "c6": Course("C", "6", None, 5),
            "c7": Course("C", "7", None, 5),
            "c8": Course("C", "8", None, 5),
            "c9": Course("C", "9", None, 5),
            "c10": Course("C", "10", None, 5),
            "c11": Course("C", "11", None, 5),
            "c12": Course("C", "12", None, 5),
            "c13": Course("C", "13", None, 5)
            }
    quarters = [ \
            Quarter([], "fall", 19), \
            Quarter([], "winter", 19), \
            Quarter([], "spring", 19) \
            ]
    timeline = Timeline(quarters, completedCourses)

    # print timeline
    printTimeline(timeline);

    # 4. create the consolidated one-path tree (skipping prior steps)
    head = Node([
        Node([
            Node([], 0, courses["c8"], {"pre":True}),
            Node([
                Node([], 0, courses["c10"], {"pre":True})
                ], 1, courses["c11"], {"pre":True})
            ], 1, courses["c5"], {"pre":True}),
        Node([
            Node([], 0, courses["c10"], {"pre":True})
            ], 1, courses["c7"], {"pre":True})
        ], 2)

    print
    printTree(head)

    # createTimeline(...)

main()
