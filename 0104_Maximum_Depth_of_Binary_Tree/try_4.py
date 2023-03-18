# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        depth = ans = 0
        stack = []
        while stack or root:
            if root:
                stack.append((root, depth))
                root = root.left
                depth += 1
            else:
                root, depth = stack.pop()
                root = root.right
                depth += 1
            
            ans = max(depth, ans)
        
        return ans
