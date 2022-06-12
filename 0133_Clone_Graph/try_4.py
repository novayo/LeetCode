"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # O(V+E) time / O(V) space
        if not node:
            return node
        
        que = collections.deque()
        cache = {} # val: node
        
        # init
        cache[node.val] = Node(node.val, [])
        que.append(node)
        
        # bfs
        while que:
            old_node = que.popleft()
            
            for nei in old_node.neighbors:
                # create unvisited node
                if nei.val not in cache:
                    cache[nei.val] = Node(nei.val, [])
                    que.append(nei)
                
                # update to current node
                cache[old_node.val].neighbors.append(cache[nei.val])
        
        return cache[node.val]