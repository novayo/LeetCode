# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # binary search
        '''
        直接用binary search去跑bst (因為左小又大)
        從頭開始往下跑，
        if node.val > target: 
            go left
        else:
            go right
            
        順便紀錄差值
        '''
        
        ans = float('inf')
        while root:
            if abs(ans-target) > abs(root.val-target):
                ans = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return ans
