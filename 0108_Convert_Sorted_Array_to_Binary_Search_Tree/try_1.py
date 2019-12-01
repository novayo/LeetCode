# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums == []: return
        def recur(i, j):
            if (i > j): return
            index = (j+i)//2
            ans = TreeNode(nums[index])
            ans.left = recur(i, index-1)
            ans.right = recur(index+1, j)
            return ans
        
        return recur(0, len(nums) - 1)
