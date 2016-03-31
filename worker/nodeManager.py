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
            if os.stat("pkl/nodes_dict.pkl").st_size > 0:
                # get the current list of nodes
                self.nodesDict = self.read("pkl/nodes_dict.pkl")
            else:
                # set to empty
                self.nodesDict = {}
        except OSError:
            # set to empty
            self.nodesDict = {}
    # @desc Saves a node of the given obj & name, overwritting the previous entry if one exists
    def save(self, node):
        if node.name:
            # add node to the dictionary regardless of its previous existence
            self.nodesDict[node.name] = True
        else:
            print "ERROR: node must have a `name` in order to be saved!"
            return
        # persist new dictionary state
        self.write(self.nodesDict, "pkl/nodes_dict.pkl")
        # persist new node itself
        self.write(node, "pkl/" + node.name + ".pkl")
    # @desc Loads a node of the given name and returns it, returns False if 
    def load(self, name):
        # check if exists
        if not name in self.nodesDict:
            return False
        else:
            # read and return it
            return self.read("pkl/" + name + ".pkl")
    # @desc Returns a list of all persisted nodes
    def loadAll(self):
        nodes = []
        for key in self.nodesDict.keys():
            nodes.append(self.load(key))
        return nodes
    # @desc Deletes a node of the given name
    def delete(self, name):
        if name in self.nodesDict:
            # delete from dict
            self.nodesDict.pop(name)
            # persist dict
            self.write(self.nodesDict, "pkl/nodes_dict.pkl")
        else:
            print "ERROR: node with name '" + name + "' does not exist!"
            return
        # delete from files
        os.remove("pkl/" + name + ".pkl")
    # ***********************************************************************************
    # @desc Writes an object to the named file
    # @param obj The object to write/save
    # @param filename The path to the obj's file
    # ***********************************************************************************
    def write(self, obj, filename):
        with open(str(filename), "wb") as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
    # ***********************************************************************************
    # @desc Reads the object from the file given by the provided name and returns that obj
    # @param filename The path to the obj's file
    # ***********************************************************************************
    def read(self, filename):
        with open(str(filename), "rb") as input:
            return pickle.load(input)

