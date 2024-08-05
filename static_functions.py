from const import *
import itertools

from node import Node

def print_state(state):
        towers = {i: [] for i in range(num_towers)}
    
        # Populate the dictionary with disks based on the state array
        for disk, tower in enumerate(state):
            towers[tower].append(disk)
        
        # Print the state of each tower
        for tower in range(num_towers):
            print(f"Tower {tower}: {sorted(towers[tower], reverse=True)}")

def allowed_pegs(state, parent_state):
        towers = [i for i in range(num_towers)]

        for i in range(len(state)):
            if state[i] != parent_state[i]:
                towers.remove(state[i])
                towers.remove(parent_state[i])
                return towers
            
def state_to_string(state):
    ans = ""
    for peg in state:
        ans += str(peg)
    return ans

def string_to_state(string):
    array_state = []
    for peg in range(len(string)):
        array_state.append(int(string[peg]))
    return array_state

def generate_complete_config(state, allowed_pegs):
    string_allow_pegs = [str(i) for i in allowed_pegs]
    combinations = itertools.product(string_allow_pegs, repeat=num_small_disk)
    combinations_list = [''.join(comb) for comb in combinations]
    return [comb+state for comb in combinations_list]

def get_initial_state(solved_node: Node):
    cur_node = solved_node
    while cur_node.parent is not None:
          cur_node = cur_node.parent
    return cur_node.state