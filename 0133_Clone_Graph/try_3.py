"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        found = {node.val: Node(node.val)}
        
        def dfs(old_node):
            
            new_node = found[old_node.val]
            
            for neighbor in old_node.neighbors:
                if neighbor.val not in found:
                    found[neighbor.val] = Node(neighbor.val)
                    dfs(neighbor)
                new_node.neighbors.append(found[neighbor.val])
                    
        dfs(node)
        return found[node.val]
