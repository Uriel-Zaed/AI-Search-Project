from node import Node
from const import *
from copy import deepcopy
from static_functions import *
import json

class A_Star_Double4():
    def __init__(self, initial_states, goal_state):
        self.initial_states = initial_states # array of string states
        self.goal_state = string_to_state(goal_state)
        with open(f'hanoi_database 4.txt', "r") as file:
            fileData  = file.read()
            self.database = json.loads(fileData)
        self.N = 0

    
    def solve(self):
        frontier = []
        for state in self.initial_states:
            frontier.append(Node(string_to_state(state), None, 0, self.hur(state)))
        explored = []
        
        while((len(frontier) > 0)):
            cur_node = frontier.pop(0)
            self.N += 1

            if cur_node.state == self.goal_state:
                return cur_node.g_n
                
            explored = self.add_node_to_explored(cur_node, explored)

            # create list of childs
            child_list = self.get_childs(cur_node)

            for child in child_list:
                if (not self.in_list(child, frontier)) and (not self.in_list(child, explored)):
                    frontier = self.add_node_to_frontier(child, frontier)
        
        return None
                    
                    
    def get_solution(self, node):
        sol = []
        while (node.parent != None):
            sol.append(node.state)
            node = node.parent
        sol.reverse()
        return sol

            
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
                        new_state = deepcopy(cur_node.state) # copy of the cur node state
                        new_state[disk] = other_peg # change peg
                        child_list.append(Node(new_state, cur_node, cur_node.g_n + 1, self.hur(state_to_string(new_state)))) # creating child

        return child_list

    def in_list(self, node, list) -> bool:
        if len(list) <= 0:
            return False
        for n in list:
            if node.state == n.state:
                if node.g_n >= n.g_n:
                    return True
        return False
        
    
    def add_node_to_frontier(self, node, frontier):
        for i, n in enumerate(frontier):
            if node.g_n + node.h_n < n.g_n + n.h_n:
                frontier.insert(i, node)
                return frontier
        frontier.append(node)
        return frontier

    
    def add_node_to_explored(self, node, explored):
        for i, n in enumerate(explored):
            if node.state == n.state:
                if node.g_n < n.g_n:
                    explored[i] = node
                    return explored
                else:
                    return explored
        explored.append(node)
        return explored

    def hur(self, state):
        return self.database[state[num_small_disk:]][0]+self.database[state[:num_small_disk]][0]