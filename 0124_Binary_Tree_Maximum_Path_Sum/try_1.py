# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def _maxPathSum(head):
            nonlocal ans
            if head == None:return 0                # 若找到底了就回傳
            left = max(0, _maxPathSum(head.left))   # 拿到左值，若是負數則不拿
            right = max(0, _maxPathSum(head.right)) # 拿到右值，若是負數則不拿
            ans = max(ans, left+right+head.val)     # 判斷三格最大的
            return max(left, right)+head.val        # 找出一個最大的值回傳給上一個root
        
        ans = -float('inf')
        _maxPathSum(root)
        return ans
