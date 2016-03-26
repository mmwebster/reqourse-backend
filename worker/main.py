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
#        Must be of type String.."pre" or "co". (optional..not used if does not contain course)
# ***********************************************************************************
class Node:
    def __init__(self, children = [], numRequired = 0, course = None, parentRel = None,
            numDescendents = None, isRoot = False):
        self.children = children
        self.numRequired = numRequired
        self.course = course
        self.parentRel = parentRel
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
# @param courses An array of courses inserted into the specific quarter
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
#        [cid]->[course]
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
    for i in range(len(timeline.quarters)):
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
        # newHead = Node([], head.numRequired, None, None, None, True)
        dfsClean(head, addedCourses)
        printTree(head)
        # 15. Return to step 5



#####################################################################################
# Main
#####################################################################################
def main():
    # create testing data
    completedCourses = {}
    courses = {
            "c4": Course("C", "4", None, 5, {"fall":True, "winter":True, "spring":True}),
            "c5": Course("C", "5", None, 5, {"fall":True, "winter":True, "spring":True}),
            "c6": Course("C", "6", None, 5, {"fall":True, "winter":True, "spring":True}),
            "c7": Course("C", "7", None, 5, {"fall":True, "winter":True, "spring":True}),
            "c8": Course("C", "8", None, 5, {"fall":True, "winter":True, "spring":True}),
            "c9": Course("C", "9", None, 5, {"fall":True, "winter":True, "spring":True}),
            "c10": Course("C", "10", None, 5, {"fall":True, "winter":True, "spring":True}),
            "c11": Course("C", "11", None, 5, {"fall":True, "winter":True, "spring":True}),
            "c12": Course("C", "12", None, 5, {"fall":True, "winter":True, "spring":True}),
            "c13": Course("C", "13", None, 5, {"fall":True, "winter":True, "spring":True})
            }
    quarters = [ \
            Quarter([], "fall", 19), \
            Quarter([], "winter", 19), \
            Quarter([], "spring", 19), \
            Quarter([], "fall", 19), \
            Quarter([], "winter", 19), \
            Quarter([], "spring", 19) \
            ]
    timeline = Timeline(completedCourses, quarters)

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
        ], 2,None,None,None,True)

    # print co-pt
    printTree(head)

    # createTimeline takes as input a consolidated one-path tree
    mapTimeline(timeline, head)

    # print timeline again
    print
    print
    printTimeline(timeline)


main()
