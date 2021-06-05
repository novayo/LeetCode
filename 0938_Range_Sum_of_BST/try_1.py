# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        if not root:
            return 0
        
        r = root.val if low <= root.val <= high else 0
        left = 0
        right = 0
        if root.val < low:
            right = self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            left = self.rangeSumBST(root.left, low, high)
        else:
            left = self.rangeSumBST(root.left, low, high)
            right = self.rangeSumBST(root.right, low, high)
        
        return r + left + right
