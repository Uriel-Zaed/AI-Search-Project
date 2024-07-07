from state import State
from node import Node

class A_Star():
    def __init__(self, initial_state, goal_state, N):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.root = Node(initial_state, None, 0, self.huer_Man(initial_state))
        self.solution = None
        self.solution_f_n = 10000000000
        self.N = N
        self.logical_steps = 0 
        self.num_of_moves = -1


    
    def solve(self):
        frontier = [self.root]
        explored = []
        
        while((len(frontier) > 0)):
            cur_node = frontier.pop(0)
            self.logical_steps += 1

            if ((cur_node.g_n+self.weight*cur_node.h_n) > self.solution_f_n):
                break

            if cur_node.state == self.goal_state:
                if ((cur_node.g_n) < self.solution_f_n):
                    self.solution = self.get_solution(cur_node)
                    self.solution_f_n = cur_node.g_n
                    self.num_of_moves = len(self.solution)-1
                continue
                
            
            explored = self.add_node_to_explored(cur_node, explored)

            # create list of childs
            child_list = self.get_childs(cur_node)

            for child in child_list:
                if (not self.in_list(child, frontier)) and (not self.in_list(child, explored)):
                    frontier = self.add_node_to_frontier(child, frontier)
        
        return self.solution
                    
                    
    def get_solution(self, node):
        sol = []
        while (node.parent != None):
            sol.append(node.state)
            node = node.parent
        sol.reverse()
        return sol

            
    def get_childs(self, cur_node):
        child_list = []
        
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
            if node.g_n + self.weight*node.h_n < n.g_n + self.weight*n.h_n:
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
        explored.append(node)
        return explored

    # Manhetten dist from each tile to his goal
    def huer(self, state: State):
        pass