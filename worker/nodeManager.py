#####################################################################################
# Imports and External Refs
#####################################################################################
import cPickle as pickle
import os



#####################################################################################
# Classes
#####################################################################################
# ***********************************************************************************
# @desc Instantiate this object to use as an interface with node persistence through pickle lib. call
#       .save to persist a node, .load to retrieve a persisted node, and .loadAll to retrieve a list
#       of all persisted nodes.
# ***********************************************************************************
class nodeManager:
    def __init__(self):
        # if nodes_dict file isn't empty or missing
        try:
            if os.stat("nodes_list.pkl").st_size > 0:
                # get the current list of nodes
                self.nodesDict = read("nodes_list.pkl")
            else:
                # set to empty
                self.nodesDict = {}
        except OSError:
            # set to empty
            self.nodesDict = {}
    # @desc Saves a node of the given obj & name, overwritting the previous entry if one exists
    def save(self, node, name):
        # add node to the dictionary regardless of its previous existence
        self.nodesDict[name] = True
        # persist new dictionary state
        self.write(self.nodesDict, "nodes_list.pkl")
        # persist new node itself
        self.write(node, name + ".pkl")
    # @desc Loads a node of the given name and returns it, returns False if 
    def load(self, name):
        # check if exists
        if not name in self.nodesDict:
            return False
        else:
            # read and return it
            return self.read(name + ".pkl")
    # @desc Returns a list of all persisted nodes
    def loadAll(self):
        nodes = []
        for key in self.nodesDict.keys():
            nodes.append(self.load(key))
        return nodes
    # ***********************************************************************************
    # @desc Writes an object to the named file
    # @param obj The object to write/save
    # @param name The name of the object to use as file name and refer to later
    # ***********************************************************************************
    def write(self, obj, filename):
        with open("pkl/" + str(filename), "wb") as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
    # ***********************************************************************************
    # @desc Reads the object from the file given by the provided name and returns that obj
    # @param name The name that was used when the obj was saved
    # ***********************************************************************************
    def read(self, filename):
        with open("pkl/" + str(filename), "rb") as input:
            return pickle.load(input)

