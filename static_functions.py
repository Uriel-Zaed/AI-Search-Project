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

def allowed_pegs(state, parent_state) -> list:
        towers = [i for i in range(num_towers)]

        for i in range(len(state)):
            if state[i] != parent_state[i]:
                towers.remove(int(state[i]))
                towers.remove(int(parent_state[i]))
                return towers
        return []

def allowed_move(state, parent_state) -> list:
        towers = []

        for i in range(len(state)):
            if state[i] != parent_state[i]:
                towers.append(int(state[i]))
                towers.append(int(parent_state[i]))
                return towers
        return []

def allowed_double_pegs(cur_node: Node):
    if cur_node.state == "2323":
         print("")
    towers = allowed_pegs(cur_node.state, cur_node.parent.state)

    secound_move = allowed_move(cur_node.parent.state, cur_node.parent.parent.state)
    towers.sort() 
    secound_move.sort()
    if towers == secound_move:
        return towers
    else:
         return [item for item in towers if item not in secound_move]
            
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

def generate_complete_config_2_layer(state, allowed_pegs):
    if len(allowed_pegs) == 1:
         return [str(allowed_pegs[0])*num_small_disk + state]
    elif len(allowed_pegs) == 2:
         fisrt = str(allowed_pegs[0])*(num_small_disk-1)
         second = str(allowed_pegs[1])
         return [fisrt + second + state, second + fisrt + state, str(allowed_pegs[0])*num_small_disk + state, str(allowed_pegs[1])*num_small_disk + state]
    else: # len 4
         return [str(num_towers-1)*num_small_disk + state]
         
def generate_complete_configless(state, allowed_pegs):
    if len(allowed_pegs) == 2:
         fisrt = str(allowed_pegs[0])*(num_small_disk-1)
         second = str(allowed_pegs[1])
         return [fisrt + second + state,
                  second + fisrt + state,
                  str(allowed_pegs[0])*num_small_disk + state,
                    str(allowed_pegs[1])*num_small_disk + state]
    else: # len 4
         return [str(num_towers-1)*num_small_disk + state]
         

def get_initial_state(solved_node: Node):
    cur_node = solved_node
    while cur_node.parent is not None:
          cur_node = cur_node.parent
    return cur_node.state