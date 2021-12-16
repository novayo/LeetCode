# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(nums):
            if not nums:
                return None
            
            middle = len(nums) // 2
            root = TreeNode(nums[middle])
            root.left = dfs(nums[:middle])
            root.right = dfs(nums[middle+1:])
            
            return root
        
        return dfs(nums)