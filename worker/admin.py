#####################################################################################
# Imports and External Refs
#####################################################################################
import worker as rq # import reqourse worker
from nodeManager import nodeManager


    
#####################################################################################
# Functions
#####################################################################################

# ***********************************************************************************
# @desc Recursive function that builds the descendents of the currently passed node then bubbles back
#       up recursively
# @param node The current head of a subtree
# ***********************************************************************************
def buildTree(node):
    # prompt to describe current node
    nodeType = raw_input("   Node type >>")
    if nodeType == "pivot":
        node.pivot == raw_input("   Node's name >>")
    # else:
        
    # prompt for children
    
    print "building..."



#####################################################################################
# Main
#####################################################################################
def main():
    print "Hello, admin"
    # instantiate node manager
    nm = nodeManager()
    # create new nodes list
    newNodes = []
    # attempt to persist node
    for node in newNodes:
        nm.save(node)
    # attempt to retrieve all nodes
    persistedNodes = nm.loadAll()
    i = 1
    # print out the current tree goals
    print "The current tree goals saved are:"
    for node in persistedNodes:
        print "  " + str(i) + ": " + str(node.name)
        i += 1

    # the action loop
    action = raw_input("Perform an action: ")
    while (action):
        # trigger correct action
        if action == "creategoal":
            newGoal = rq.Node()
            newGoal.isHead = True
            # get name
            pivotName = raw_input("  " + action + ": goal's name >>")
            if pivotName:
                newGoal.pivot = pivotName
                # run the creation script
                buildTree(newGoal)
            else:
                print "Error: invalid name!"
        else:
            print "ERROR: Invalid action name!"
        # prompt new action
        action = raw_input("Perform an action: ")
