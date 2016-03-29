#####################################################################################
# Imports and External Refs
#####################################################################################
import worker as rq # import reqourse worker
from nodeManager import nodeManager


    
#####################################################################################
# Functions
#####################################################################################



#####################################################################################
# Main
#####################################################################################
def main():
    print "Hello, admin"
    # print out the current tree goals
    name = raw_input("Please enter your name: ")
    print "Hi, " + str(name)
    # create nodes list
    newGoals = [rq.Node([], None, 22), rq.Node([], None, 33)]
    # instantiate node manager
    nm = nodeManager()
    # attempt to persist node
    nm.save(goal1, "goal1")
    # del node in current scope
    del goal1
    # attempt to retrieve node
    newGoal = nm.load("goal1")
    print "Loaded node's numRequired=" + str(newGoal.numRequired)



    ### Now need to MAKE SURE nodeManager is working..then proceed to do admin side of final flow


    ## !!!! abstracted out the nodeManager, now need to implement...(follow the flow)
