"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        
        def dfs(node, visited):
            if not node:
                return node

            if node in visited:
                return visited[node]
            
            tmp = Node(node.val)
            visited[node] = tmp
            
            if node.neighbors:
                for n in node.neighbors:
                    tmp.neighbors.append(dfs(n, visited))
        
            return tmp
        
        return dfs(node, visited)
