# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0
        queue = collections.deque()
        queue.append((root, 0, 1)) # node, level, score
        
        cur_level = -1
        _min = float('inf')
        while queue:
            node, level, score = queue.pop()
            
            if level > cur_level:
                cur_level = level
                _min = score
            
            ans = max(ans, score - _min + 1)
            
            if node.left:
                queue.appendleft((node.left, level+1, score*2-1))
            
            if node.right:
                queue.appendleft((node.right, level+1, score*2))
        
        return ans
