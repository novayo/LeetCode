# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        queue = collections.deque()
        queue.append((p, q))
        
        while queue:
            _p, _q = queue.popleft()
            
            if _p == None and _q == None:
                continue
            elif _p == None or _q == None:
                return False
            
            if _p.val != _q.val:
                return False
            
            queue.append((_p.left, _q.left))
            queue.append((_p.right, _q.right))
        
        return True
