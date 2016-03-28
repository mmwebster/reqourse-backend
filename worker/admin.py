#####################################################################################
# Imports and External Refs
#####################################################################################
import cPickle as pickle
import worker as rq # import reqourse worker

#####################################################################################
# Classes
#####################################################################################

# ***********************************************************************************
# @desc A simple class for storing a list of nodes, b/c pickle requires an obj
# ***********************************************************************************
class nodesListObj:
    def __init__(self, nodes = []):
        self.nodes = nodes
        
# ***********************************************************************************
# @desc An object in which to hold all information about the available nodes for reading and provides
#       an interface for properly saving nodes
# @param nodes A list of all the nodes available for reading
# ***********************************************************************************
class nodeManager:
    def __init__(self):
        # get the current list of nodes, actual list is nested inside the obj
        self.nodesListObj = read("nodes_list") # 
    # @desc Saves a node of the given obj & name, overwritting the previous entry if one exists
    def save(self, node, name):
        # write the object to the file
        write(node, (name + ".pkl"))
        # add it to the nodes list in the instance of nodeManager and update them in file
        ##!!! now almost done..need to add to persist
    # @desc Loads a node of a the given name and returns it
    def load(self, name):
        

# !!!! left off
# -> finishing up interface for writing and reading objs, then saving and loading nodes



#####################################################################################
# Functions
#####################################################################################

# ***********************************************************************************
# @desc Writes an object to the named file
# @param obj The object to write/save
# @param name The name of the object to use as file name and refer to later
# ***********************************************************************************
def write(obj, filename):
    with open("pkl/" + str(filename), "wb") as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

# ***********************************************************************************
# @desc Reads the object from the file given by the provided name and returns that obj
# @param name The name that was used when the obj was saved
# ***********************************************************************************
def read(filename):
    with open("pkl/" + str(filename), "rb") as input:
        return pickle.load(input)
    
# ***********************************************************************************
# @desc Saves a node and all of its contents save that it can be read later
# @param node The object to write/save
# @name The name of the object to use as file name and refer to later
# ***********************************************************************************



#####################################################################################
# Main
#####################################################################################
def main():
    print "Hello, admin"
    # print out the current tree goals
    name = raw_input("Please enter your name: ")
    print "Hi, " + str(name)
    node = rq.Node([], None, 1)
    write(node, "node")
    del node
    node2 = read("node")
    print "The read node's numReq is " + str(node2.numRequired)
