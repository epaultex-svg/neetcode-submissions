"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        seen = set()
        oldToNew = {}
        
        def dfs(node):
            copy = Node(node.val)
            if node in seen: 
                return copy
            oldToNew[node] = copy
            seen.add(node)
            
            for nbr in node.neighbors:
                nbrCopy = dfs(nbr)
                copy.neighbors.append(oldToNew[nbr])
            
            return copy

        return dfs(node)

