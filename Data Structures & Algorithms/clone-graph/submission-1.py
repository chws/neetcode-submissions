"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # try in iterative way
        if not node:
            return None
        cloned = {node: Node(node.val)}
        stack = [node]

        while stack:
            curr = stack.pop()
            new_node = cloned[curr]
            for neighbor in curr.neighbors:
                if neighbor in cloned:
                    new_neighbor = cloned[neighbor]
                else:
                    new_neighbor = Node(neighbor.val)
                    cloned[neighbor] = new_neighbor
                    stack.append(neighbor)
                new_node.neighbors.append(new_neighbor)
        return cloned[node]