# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def add(n1, n2, direction):
            if n1 not in graph:
                graph[n1] = {}
            graph[n1][direction] = n2
        
        graph = {}
        
        def recr(node):
            if not node:
                return
            
            if node.left:
                add(node.val, node.left.val, 'L')
                add(node.left.val, node.val, 'U')
                recr(node.left)
            if node.right:
                add(node.val, node.right.val, 'R')
                add(node.right.val, node.val, 'U')
                recr(node.right)
            
        recr(root)
        cache = set([startValue])
        que = [(startValue, '')]
        while que:
            next_que = []
            
            for node, path in que:
                for direction in 'LRU':
                    if direction not in graph[node]:
                        continue
                    
                    nei = graph[node][direction]
                    if nei in cache:
                        continue
                    
                    if nei == destValue:
                        return path + direction
                    
                    cache.add(nei)
                    next_que.append((nei, path + direction))
            que = next_que
        return ''
            
