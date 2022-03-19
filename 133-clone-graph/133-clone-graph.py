"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited={}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        #termination condition
        if node in self.visited:
            return self.visited[node]
        
        #create a clone node for given node
        clone_node=Node(node.val,[])
        
        #key is original node and value being the clone node.
        self.visited[node]=clone_node
        
        #recursion step
        if node.neighbors:
            clone_node.neighbors=[self.cloneGraph(n) for n in node.neighbors]
        
        return clone_node