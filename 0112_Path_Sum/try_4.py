# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = []
        curSum = 0
        
        while root or stack:
            if root:
                # visit
                curSum += root.val
                
                if (root.left is None and root.right is None) \
                        and curSum == targetSum:
                    return True
                
                stack.append((root, curSum))
                root = root.left
            else:
                root, curSum = stack.pop()
                root = root.right
        
        return False
