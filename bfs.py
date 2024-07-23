from node import Node
from const import *
from copy import deepcopy
from static_functions import *

class BFS():
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.root = Node(initial_state, None, 0)

    
    def solve(self):
        frontier = [self.root]
        explored = []
        database = {} # key: configuration, value: (g(configuration), array of allowed pegs))
        
        while((len(frontier) > 0)):
            cur_node = frontier.pop(0)  

            if cur_node.state == self.initial_state:
                database[state_to_string(cur_node.state)] = (cur_node.g_n, [i for i in range(num_towers)])  
            else:
                database[state_to_string(cur_node.state)] = (cur_node.g_n, allowed_pegs(cur_node.state,cur_node.parent.state))             
            
            explored.append(cur_node.state)

            # create list of childs
            child_list = self.get_childs(cur_node)

            for child in child_list:
                if (not self.in_list(child, frontier)) and (child.state not in explored):
                    frontier.append(child)
        
        return database
            
    def get_childs(self, cur_node):
        child_list = []
        
        min_disk_per_peg = [-1]*num_towers
        for peg in range(num_towers):
            for i,v in enumerate(cur_node.state):
                if v == peg:
                    min_disk_per_peg[peg] = i
                    break
        
        for peg,disk in enumerate(min_disk_per_peg):
            for other_peg,other_disk in enumerate(min_disk_per_peg):
                if peg != other_peg and disk != -1: # checks if not same peg and have a disk in that peg
                    if disk < other_disk or other_disk == -1: # check if possible move
                        # new_state = deepcopy(cur_node.state) # copy of the cur node state
                        new_state = [d for d in cur_node.state] # copy of the cur node state
                        new_state[disk] = other_peg # change peg
                        child_list.append(Node(new_state, cur_node, cur_node.g_n + 1)) # creating child

        return child_list

    def in_list(self, node, list) -> bool:
        if len(list) <= 0:
            return False
        for n in list:
            if node.state == n.state:
                return True
        return False
    
    