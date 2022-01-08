"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        table = {node.val: Node(node.val)}
        queue = [node]
        while queue:
            _node = queue.pop()
            
            root = table[_node.val]
            
            for neighbor in _node.neighbors:
                if neighbor.val not in table:
                    table[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                root.neighbors.append(table[neighbor.val])
        
        return table[node.val]
            
            
            
            