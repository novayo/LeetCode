# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        visited_dict = collections.Counter()
        visited_dict[0] = 1
        ans = 0
        
        def dfs(node, curSum):
            nonlocal ans
            
            if not node:
                return
            
            curSum += node.val
            ans += visited_dict[curSum - targetSum]
            
            visited_dict[curSum] += 1
            
            dfs(node.left, curSum)
            dfs(node.right, curSum)
            
            visited_dict[curSum] -= 1
            
        dfs(root, 0)
        return ans
