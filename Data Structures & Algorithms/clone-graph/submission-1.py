"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldnew = {}

        def clone(node):
            if not node:
                return None
            if node in oldnew:
                return oldnew[node]
            copy = Node(node.val)
            oldnew[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            return copy
        return clone(node)