#####################################################################################
# GENERAL NOTES
#####################################################################################
# 1. Course tuples were removed and now referred to as nodes (but aren't entirely the same)
# 2. Style guidelines: For every new section, enclose the same hash formation as seen elsewhere,
#    for every new class or function definition enclose with the same asterisks seen elsewhere.
#    The end of a section should be followed by three new lines, while the everywhere else different
#    component should be delimited a single new line.
# 3. Numbered comments are referring to discrete steps in the flow-charted algorithms



#####################################################################################
# Imports and External Refs
#####################################################################################

import copy



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
# @desc A basic stack implementation (really just for clarity..it's just an array)
# ***********************************************************************************
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

# ***********************************************************************************
# @desc A node in one of the course-dependent trees; acts like a container for courses that may or
#       may not be filled.
# @param children List of all child nodes
# @param numRequired The number of the children that must be satisfied in the tree to take this
#        course
# @param course A single course definition (optional) for this node
# @param parentRel The type of relationship between the course in this node and that in its parent.
#        Must be of type String.."pre" or "co". (optionally set to None..not used if does not
#        contain course)
# ***********************************************************************************
class Node:
    def __init__(self, children = [], course = None, numRequired = 0, parentRel = "pre",
            numDescendents = None, isRoot = False):
        self.children = children
        self.course = course
        self.numRequired = numRequired
        self.parentRel = {parentRel:True} # made so that dict. format is not required
        self.numDescendents = numDescendents
        self.isRoot = isRoot

# ***********************************************************************************
# @desc A single course and its attributes
# @param subject The subject code (string) used to catagorize the course by
# @param number The number used to uniquely identify a course within a subject
# @param title The name of the course as it is displayed and used
# @param seasonsOffered A dictionary with [season name]->[boolean] pairs...when the course is offered
# ***********************************************************************************
class Course:
    def __init__(self, subject, number, title, units, seasonsOffered = {}, concurrentCourse = None):
        self.subject = subject
        self.number = number
        self.title = title
        self.units = units
        self.seasonsOffered = seasonsOffered
        self.concurrentCourse = concurrentCourse
    def getCid(self):
        return self.subject + str(self.number)
    def getTotalUnits(self):
        totalUnits = 0
        if self.concurrentCourse != None:
            totalUnits += self.concurrentCourse.units
        totalUnits += self.units
        return totalUnits

# ***********************************************************************************
# @desc A single quarter in the Timeline
# @param courses An array of courses inserted into the specific quarter. Must be of type Course
# @param season A string containing the season this quarter is in..used with course season dict.
# @param maxUnits the max number of units desired for this quarter
# ***********************************************************************************
class Quarter:
    def __init__(self, courses = [], season = None, maxUnits = 19):
        assert all(isinstance(course, Course) for course in courses)
        self.courses = courses
        self.season = season
        self.maxUnits = maxUnits
    # @desc Returns the total number of units currently stored in this quarter
    def getTotalUnits(self):
        totalUnits = 0
        for course in self.courses:
            totalUnits += course.getTotalUnits()
        return totalUnits

# ***********************************************************************************
# @desc The planned out courses in their quarter with respect their seasons
# @param quarters Contains of the currently planned out quarters
# @param completedCourses Contains a bucket (dictionary) of all completed courses in the format
#        [cid]->[boolean]
# @param quarters List of all quarter in the Timeline (length may be greater than currentQuarter)
# @param currentQuarter Index of the quarter that's currently being worked on
# @param startingSeason The default season of the first quarter in the timeline
# ***********************************************************************************
class Timeline:
    def __init__(self, completedCourses = {}, quarters = [], currentQuarter = 0,
            startingSeason = "fall"):
        assert all(isinstance(quarter, Quarter) for quarter in quarters)
        self.completedCourses = completedCourses
        self.quarters = quarters
        self.currentQuarter = currentQuarter
        self.startingSeason = startingSeason
    # @desc Return the # of populated quarters
    def getNumQuarters(self):
        return len(self.quarters)
    # @desc Returns a boolean of whether or not the passed course has been completed
    # @param course The course to test for having been completed
    def isCompleted(self, course):
        if course.getCid() in self.completedCourses:
            return True
        else:
            return False
    # @desc Return a boolean of whether or not the passed course is in a quarter `offset` from the
    #       current
    # @param course The course to search for
    # @param parentRel The requirement type between the course that must be satisfied (`course`) and
    #        the one that needs it to be satisfied. Must be of type String
    def isSatisfied(self, course, parentRel):
        # check if is in completed courses
        if self.isCompleted(course):
            return True
        # check if is in a previous (or possibly current) quarter
        offset = -1 if parentRel == "pre" else 0
        endIndex = self.currentQuarter+offset
        endIndex = 0 if endIndex < 0 else endIndex
        for quarter in self.quarters[0:endIndex]:
            for c in quarter.courses:
                if course.getCid() == c.getCid():
                    return True
        return False
    # @desc Returns a string for the season of the current quarter (end of quarters list)
    def getCurrentSeason(self):
        if not self.quarters:
            return self.startingSeason
        else:
            return self.quarters[self.currentQuarter].season



#####################################################################################
# Function definitions
#####################################################################################

# ***********************************************************************************
# @desc Prints out every quarter in the timeline and every course within every quarter
# @param timeline The timeline to print out
# ***********************************************************************************
def printTimeline(timeline):
    assert isinstance(timeline, Timeline)
    print("Timeline:")
    year = 1
    for i in range(len(timeline.quarters)):
        if i % 3 == 0:
            print "- - - - - - Year " + str(year) + " - - - - - -"
            year += 1
        print(" Qtr " + str(i + 1) + ", " + str(timeline.quarters[i].getTotalUnits()) \
                + " units(s), (" + timeline.quarters[i].season + ")")
        for course in timeline.quarters[i].courses:
            print(" -" + course.subject + str(course.number))

# ***********************************************************************************
# @desc Prints out a tree given the head node. Uses a BFS type implementation w/ mods.
# @param head The head of the tree, of type Node
# ***********************************************************************************
def printTree(head):
    print "- - - - - - - Printing Tree - - - - - - - - -"
    currentLevel = [head]
    while currentLevel:
        nextLevel = []
        for node in currentLevel:
            if not node.course == None:
                print "(" + str(id(node)) + "->numReq: " + str(node.numRequired) + ", cid: " + \
                        node.course.getCid() + ")",
            else:
                print "(" + str(id(node)) + "->numReq: " + str(node.numRequired) + ", cid: ..)",

            for child in node.children:
                nextLevel.append(child)
        print # add new line
        print
        currentLevel = nextLevel # proceed to next level

# ***********************************************************************************
# @desc Prints out a stack of nodes according to their corresponding cids
# @param stack The stack to print, must be of type Stack
# ***********************************************************************************
def printPriorityStack(stack):
    assert isinstance(stack, Stack)
    print "- - -  - Printing Priority Stack - - - - -"
    print "| root | ",
    for node in stack.items:
        if node.course != None:
            print node.course.getCid() + " | ",
        else:
            print "root | ",
    print # add the newline

# ***********************************************************************************
# @desc Prints out a dictionary
# @param dictionary The dictionary
# ***********************************************************************************
def printDictionary(dictionary):
    assert isinstance(dictionary, dict)
    keys = dictionary.keys()
    print "- - - - - Printing Dictionary - - - - -"
    print "{ ",
    for key in keys:
        print "'" + key + "': " + str(dictionary[key]) + " , ",
    print "}"

# ***********************************************************************************
# @desc Basic BFS implementation, where some function can be called with the current node (and its
#       own args) everytime one is visited
# @param node The head of the tree to operate on
# @param function The function to be called for every node visit (dequeue)
# @param *args Any arguments that the function needs outside of the node
# ***********************************************************************************
def bfs(node, function, *args):
    assert isinstance(node, Node)
    queue = Queue()
    queue.enqueue(node)

    # proceed with BFS, printing element along the way
    while not queue.isEmpty():
        n = queue.dequeue()
        # perform passed function
        function(n, *args)
        # queue every child of n
        for child in n.children:
            queue.enqueue(child)

# ***********************************************************************************
# @desc DFS-postorder implementation for sorting nodes in a tree from least to most descendents
# @param node The head of the current sub-tree. Must be of type Node
# @param order Boolean where False:Ascending and True:Descending order
# ***********************************************************************************
def dfsSort(node, order):
    # default node's numDescendents to zero
    node.numDescendents = 0
    # for every child of node
    for child in node.children:
        # visit the child
        dfsSort(child, order)
        # inc. num of descendents on node by this child's descendents and the child itself
        node.numDescendents += child.numDescendents + 1
    # sort this node's children
    node.children.sort(key=lambda x: x.numDescendents, reverse=order)

# ***********************************************************************************
# @desc DFS-postorder implementation for removing all nodes from tree that match dict. entries. The
#       implementation isn't especially clean due to the nature of deleting members of a list while
#       you are iterating through it (must redefine current index and such).
# @param node The head of the current sub-tree. Must be of type Node
# @param removables Dict. of items to remove in form [cid]->[course]
# ***********************************************************************************
def dfsClean(node, removables):
    i = 0
    endIndex = len(node.children)
    while i < endIndex:
        # if child matches, remove it
        if node.children[i].course.getCid() in removables:
            del node.children[i]
            # fix i so that it doesn't skip over the next item
            i -= 1
            endIndex -= 1
        else:
            # otherwise, visit it
            dfsClean(node.children[i], removables)
        i += 1

# ***********************************************************************************
# @desc DFS-postorder implementation that builds out all of the subtrees of node by, when
#       encountering a child node, looking up its child nodes in courseNodeDict
#       and then recurring on node with newly defined subtrees. This allows for input of just
#       course nodes and their immediate children to get a fully fledged gen-path or one-path
#       tree (gen-path currently untested, but shouldn't matter b/c based off of children only).
# @param node The head of the current sub-tree. Must be of type Node
# @param courseNodes A 1 dimensional array of nodes w/ defined subtrees
# @param courseNodeDict Dict. of [cid]->[index in courseNodes] used as a lookup table
# ***********************************************************************************
def dfsConnectNodeSubtrees(node, courseNodes, courseNodeLookupDict):
    # for every child in node
    for child in node.children:
        # lookup child in dict. and use to define children of child
        child.children = courseNodes[courseNodeLookupDict[child.course.getCid()]].children
        # dive into children
        dfsConnectNodeSubtrees(child, courseNodes, courseNodeLookupDict)





# ***********************************************************************************
# @desc Creates and returns a priority stack of all the nodes in the passed tree. This is done by
#       performing a basic BFS, where pushToPriorityStack(node) is called for every visit (dequeue)
#       of a node. Root node is not added to stack.
# @param node The head of the current sub-tree. Must be of type Node
# ***********************************************************************************
def createPriorityStack(node):
    # @desc Pushes a node into the priority stack
    # @param node The node to be pushed
    def pushToPriorityStack(node):
        if not node.isRoot:
            priorityStack.push(node)

    # init final priority stack
    priorityStack = Stack()
    # populate priority stack
    bfs(node, pushToPriorityStack)
    # return it
    return priorityStack

# ***********************************************************************************
# @desc Evaluates a node (and associated course) against a current quarter in timeline
# @param node The node to perform eval on
# @param timeline A reference to the currently mapped out timeline
# ***********************************************************************************
def courseDoesEval(node, timeline):
    # confirm correct types
    assert isinstance(node, Node)
    assert isinstance(timeline, Timeline)
    # 1. course in completed courses?
    if timeline.isCompleted(node.course):
        return False
    # 2. is it offered this quarter?
    if not node.course.seasonsOffered[timeline.getCurrentSeason()]:
        return False
    # 3/4. All reqs satisfied? (children with "pre" and "co" as parentRel)
    for child in node.children:
        if not timeline.isSatisfied(child.course, child.parentRel):
            return False
    # 5/6. Make sure that quarter unit limit has not been exceeded (including potential concurrent
    #      courses)
    totalPotentialUnits = timeline.quarters[timeline.currentQuarter].getTotalUnits() + \
            node.course.getTotalUnits()
    if totalPotentialUnits > timeline.quarters[timeline.currentQuarter].maxUnits:
        return False # collectively exceed unit limit
    # All tests passed
    return True

# ***********************************************************************************
# @desc Maps a path across quarters in the timeline
# @param timeline The timeline to operate on
# @param headOrigin The head of the consolidated one-path tree. This object is copied so that the
#        source tree is not mutated.
# ***********************************************************************************
def mapTimeline(timeline, headOrigin):
    assert isinstance(timeline, Timeline)
    assert isinstance(headOrigin, Node)
    head = copy.deepcopy(headOrigin)
    addedCourses = {} # dict. of courses used to quickly check if course has already been placed
    timeline.currentQuarter = 0 # always start mapping (or remapping) at the first quarter
    # 5. return once all descendents of head have been placed
    while len(head.children) > 0:
        # 6. recursively sort tree (DFS) by number of children, from least->most b/c a
        #    BFS is left->right, top->down and a stack is LIFO..making the bottom right
        #    node appear first
        dfsSort(head, False)
        printTree(head)
        # 7. populate "priority stack" about the head of tree
        priorityStack = createPriorityStack(head)
        printPriorityStack(priorityStack)
        # 8. operate on each node in stack unless exit condition evals
        for i in range(len(priorityStack.items)):
            node = priorityStack.pop()
            # 9. Node's course exists in addedCourses dict.?
            if node.course.getCid() in addedCourses:
                continue # move to next node in stack
            # 10. Node's course passes eval for current quarter?
            if not courseDoesEval(node, timeline):
                continue # move to next node in stack
            # 11. Add course and any concurrents to addedCourses dict. & current quarter in
            #     timeline. Undecided about the concurrent, so not adding that for now
            addedCourses[node.course.getCid()] = node.course
            timeline.quarters[timeline.currentQuarter].courses.append(node.course)
            # 12. Current quarter's total units equal quarter's maxUnits?
            if not timeline.quarters[timeline.currentQuarter].getTotalUnits == \
                    timeline.quarters[timeline.currentQuarter].maxUnits:
                continue # move to next node in stack
            else:
                break # move to next quarter, recomputing priority stack
        # 13. Increment current quarter
        timeline.currentQuarter += 1 # move to next quarter
        # 13.2. Make sure that quarter exists
        if len(timeline.quarters) == timeline.currentQuarter:
            seasonsMap = {"fall":0, "winter":1, "spring":2}
            seasons = {0:"fall", 1:"winter", 2:"spring"}
            oldSeason = timeline.quarters[timeline.currentQuarter-1].season
            newSeason = seasons[(seasonsMap[oldSeason] + 1)%3]
            timeline.quarters.append(Quarter([], newSeason))
        # 14. Mutate and cleanup the tree copy, `head`, from any nodes matching courses in dict.
        # temp for testing
        printDictionary(addedCourses)
        dfsClean(head, addedCourses)
        printTree(head)
        # 15. Return to step 5



#####################################################################################
# Main
#####################################################################################
# temporary function to do a simple task
def appendAndDict(someList, someDict, i, node):
    someList.append(node)
    someDict[node.course.getCid()] = i
    i += 1
    return i
def main():
    # dictionary of all testing courses
    course = {
            'MATH19A': Course("MATH", "19A", None, 5, {"fall":True, "winter":True, "spring":True}),        # i=0
            'MATH19B': Course("MATH", "19B", None, 5, {"fall":True, "winter":True, "spring":True}),
            'MATH23A': Course("MATH", "23A", None, 5, {"fall":True, "winter":True, "spring":True}),
            'CMPE8': Course("CMPE", "8", None, 5, {"fall":True, "winter":False, "spring":False}),
            'CMPE16': Course("CMPE", "16", None, 5, {"fall":True, "winter":True, "spring":True}),
            'CMPE107': Course("CMPE", "107", None, 5, {"fall":False, "winter":True, "spring":True}),
            'CMPE12': Course("CMPE", "12", None, 5, {"fall":True, "winter":True, "spring":True}),
            'CMPE12L': Course("CMPE", "12L", None, 2, {"fall":True, "winter":True, "spring":True}),
            'CMPE13': Course("CMPE", "13", None, 5, {"fall":False, "winter":True, "spring":True}),
            'CMPE13L': Course("CMPE", "13L", None, 2, {"fall":False, "winter":True, "spring":True}),
            'CMPE9': Course("CMPE", "9", None, 5, {"fall":False, "winter":True, "spring":False}),         # i=10
            'CMPE115': Course("CMPE", "115", None, 5, {"fall":False, "winter":False, "spring":True}),
            'CMPE100': Course("CMPE", "100", None, 5, {"fall":False, "winter":True, "spring":True}),
            'CMPE100L': Course("CMPE", "100L", None, 2, {"fall":False, "winter":True, "spring":True}),
            'CMPE121': Course("CMPE", "121", None, 5, {"fall":True, "winter":False, "spring":True}),
            'CMPE121L': Course("CMPE", "121L", None, 2, {"fall":True, "winter":False, "spring":True}),
            'CMPE118': Course("CMPE", "118", None, 5, {"fall":True, "winter":False, "spring":False}),
            'CMPE118L': Course("CMPE", "118L", None, 2, {"fall":True, "winter":False, "spring":False}),
            'CMPE141': Course("CMPE", "141", None, 5, {"fall":True, "winter":False, "spring":False}),
            'CMPE167': Course("CMPE", "167", None, 5, {"fall":False, "winter":True, "spring":False}),
            'CMPE167L': Course("CMPE", "167L", None, 2, {"fall":False, "winter":True, "spring":False}),     # i=20
            'CMPE216': Course("CMPE", "216", None, 5, {"fall":False, "winter":False, "spring":True}),
            'CMPE80E': Course("CMPE", "80E", None, 5, {"fall":False, "winter":False, "spring":True}),
            'CMPE185': Course("CMPE", "185", None, 5, {"fall":True, "winter":True, "spring":True}),
            'CMPE129A': Course("CMPE", "129A", None, 5, {"fall":True, "winter":False, "spring":False}),
            'CMPE129B': Course("CMPE", "129B", None, 5, {"fall":False, "winter":True, "spring":False}),
            'CMPE129C': Course("CMPE", "129C", None, 5, {"fall":False, "winter":False, "spring":True}),
            'EE103': Course("EE", "103", None, 5, {"fall":True, "winter":False, "spring":True}),
            'EE103L': Course("EE", "103L", None, 2, {"fall":True, "winter":False, "spring":True}),
            'EE101': Course("EE", "101", None, 5, {"fall":True, "winter":True, "spring":False}),
            'EE101L': Course("EE", "101L", None, 2, {"fall":True, "winter":True, "spring":False}),        # i=30
            'AMS10': Course("AMS", "10", None, 5, {"fall":True, "winter":False, "spring":True}),
            'AMS20': Course("AMS", "20", None, 5, {"fall":False, "winter":True, "spring":True}),
            'CMPS12B': Course("CMPS", "12B", None, 5, {"fall":True, "winter":True, "spring":False}),
            'CMPS12M': Course("CMPS", "12M", None, 2, {"fall":True, "winter":True, "spring":False}),
            'CMPS101': Course("CMPS", "101", None, 5, {"fall":True, "winter":True, "spring":True}),
            'PHYS5A': Course("PHYS", "5A", None, 5, {"fall":True, "winter":False, "spring":False}),
            'PHYS5L': Course("PHYS", "5L", None, 1, {"fall":True, "winter":False, "spring":False}),
            'PHYS5C': Course("PHYS", "5C", None, 5, {"fall":False, "winter":False, "spring":True}),
            'PHYS5N': Course("PHYS", "5N", None, 1, {"fall":False, "winter":False, "spring":True})        # i=39
            }

    # some vars
    uniqueCourseNodes = [] # list that will contain all unique course nodes below
    courseNodeLookupDict = {} # dict used to lookup course node in `uniqueCourse` by its cid
    i = 0 # index to inc. as val in dict: [cid]->[index]
    head = Node([],None,8,None,None,True) # head of the final tree passed mapTimeline
    # all unique course nodes and their immediate children (no uncertainty)
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([], course["CMPE8"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPE8"])], course["CMPE12"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPE12"])], course["CMPE13"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([], course["MATH19A"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["MATH19A"])], course["MATH19B"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPE13"])], course["CMPS12B"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["MATH19A"])], course["CMPE16"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([], course["AMS10"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["MATH19A"],0,"co")], course["PHYS5A"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["MATH19B"])], course["MATH23A"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["MATH19B"]),Node([],course["AMS10"])], course["AMS20"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["PHYS5A"]),Node([],course["MATH19B"])], course["PHYS5C"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPS12B"]),Node([],course["AMS10"]),Node([],course["MATH19B"]),Node([],course["CMPE16"])], course["CMPS101"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPE12"])], course["CMPE100"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["PHYS5C"]),Node([],course["AMS20"],0,"co")], course["EE101"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["EE101"],0,"co"),Node([],course["CMPE100"])], course["CMPE118"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPE16"]),Node([],course["MATH23A"])], course["CMPE107"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["MATH19A"]),Node([],course["AMS10"]),Node([],course["PHYS5A"])], course["CMPE9"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPE9"]),Node([],course["AMS10"]),Node([],course["MATH19B"])], course["CMPE115"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPE12"]),Node([],course["EE101"]),Node([],course["CMPE100"]),Node([],course["CMPE13"])], course["CMPE121"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPE9"])], course["CMPE216"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["EE101"]),Node([],course["AMS20"])], course["EE103"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPE185"],0,"co"),Node([],course["CMPE121"],0,"co")], course["CMPE129A"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["EE103"])], course["CMPE141"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPE12"])], course["CMPE185"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPE129A"])], course["CMPE129B"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPE13"]), Node([],course["EE103"])], course["CMPE167"]))
    i = appendAndDict(uniqueCourseNodes, courseNodeLookupDict, i, Node([Node([],course["CMPE129B"])], course["CMPE129C"]))

    # connect all subtrees so that can sort uniqueCourseNodes by num descendents
    uniqueNodesHead = Node(uniqueCourseNodes)
    printTree(uniqueNodesHead)
    dfsConnectNodeSubtrees(uniqueNodesHead, uniqueCourseNodes, courseNodeLookupDict)
    # printDictionary(courseNodeLookupDict)
        # ..all sub tree have been formed, now sort from least to most descendents
    # sort by num descendents
    dfsSort(uniqueNodesHead, False)
    # print immediate children of head in list of unique nodes ordered by #descendents in ascending order
    print "New ordering"
    print "[ ",
    for i in range(len(uniqueNodesHead.children)):
        print uniqueNodesHead.children[i].course.getCid(),
        if i < len(uniqueNodesHead.children)-1:
            print ",",
    print " ]"
    print

    # # Now get the consolidated one path tree from these one path subtrees
    descendents = {} # and roots children at `head.children`
    for node in uniqueNodesHead.children:
        if not node.course.getCid() in descendents:
            # add its children to the unique descendents
            for child in node.children:
                descendents[child.course.getCid()] = True
            # add the node to head's children
            head.children.append(node)
            # clean head's children of any nodes now present in unique descendents
            i = 0; length = len(head.children) # must do this method b/c removing items from the list while iterating
            while (i < length):
                if head.children[i].course.getCid() in descendents:
                    del head.children[i]
                    i -= 1; length -= 1 # decrement counter and length after removing item
                i += 1

    print "Immediate children of head of consolidated one-path tree"
    print "[ ",
    for i in range(len(head.children)):
        print head.children[i].course.getCid(),
        if i < len(head.children)-1:
            print ",",
    print " ]"
    print

    # completedCourses = {"AMS10":True, "AMS20":True, "CHEM1A":True, "CMPE100":True, "CMPE12":True, "CMPE13":True, "CMPE16":True, "CMPE8":True, "CMPS12B":True, "MATH19A":True, "MATH19B":True, "MATH23A":True, "PHYS5A":True, "PHYS5C":True}
    completedCourses = {}
    quarters = [ \
            Quarter([], "fall", 10), \
            Quarter([], "winter", 10), \
            Quarter([], "spring", 19), \
            Quarter([], "fall", 19), \
            Quarter([], "winter", 19), \
            Quarter([], "spring", 19), \
            Quarter([], "fall", 19), \
            Quarter([], "winter", 19), \
            Quarter([], "spring", 19), \
            Quarter([], "fall", 19), \
            Quarter([], "winter", 19), \
            Quarter([], "spring", 19), \
            Quarter([], "fall", 19), \
            Quarter([], "winter", 19), \
            Quarter([], "spring", 19), \
            Quarter([], "fall", 19), \
            Quarter([], "winter", 19), \
            Quarter([], "spring", 19)
            ]
    timeline = Timeline(completedCourses, quarters)

    # print timeline
    print "Timeline knot:"
    printTimeline(timeline);

    # print co-pt
    print "Current co-pt:"
    printTree(head)

    # createTimeline takes as input a consolidated one-path tree
    mapTimeline(timeline, head)

    # print timeline again
    print
    print "Finished timeline!!!:"
    printTimeline(timeline)

main()
