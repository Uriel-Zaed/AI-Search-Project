class Node():
    def __init__(self, state, parent, g_n, h_n=0):
        self.state = state
        self.parent = parent
        self.g_n = g_n
        self.h_n = h_n
        
    def __lt__(self, other):
        return (self.g_n + self.h_n) < (other.g_n + other.h_n)

    def __eq__(self, other):
        return self.state == other.state and (self.g_n + self.h_n) == (other.g_n + other.h_n)
