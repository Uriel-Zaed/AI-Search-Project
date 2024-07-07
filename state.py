from const import *

class State():
    def __init__(self, towers_state):
        self.towers_state = towers_state # Array that the index represent the disk and the number represent tower number

    def print(self):
        towers = {i: [] for i in range(num_towers)}
    
        # Populate the dictionary with disks based on the towers_state array
        for disk, tower in enumerate(self.towers_state):
            towers[tower].append(disk)
        
        # Print the state of each tower
        for tower in range(num_towers):
            print(f"Tower {tower}: {sorted(towers[tower], reverse=True)}")
            

    def __eq__(self, __value) -> bool:
        return self.towers_state == __value.towers_state