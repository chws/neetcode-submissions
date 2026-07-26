"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # given adjacnecy list, visit all the nodes and copy it
        cloned = {}

        def clone_node(node):
            if not node:
                return None
            
            new_node = Node(node.val)
            cloned[node] = new_node
            for neighbor in node.neighbors:
                if neighbor in cloned:
                    new_neighbor = cloned[neighbor]
                else:
                    new_neighbor = clone_node(neighbor)
                new_node.neighbors.append(new_neighbor)
            return new_node
        
        return clone_node(node)
