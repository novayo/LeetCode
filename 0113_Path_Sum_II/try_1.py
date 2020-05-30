# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = [] 
        
        def dfs(node, count, List):
            if not node:
                return

            count += node.val
                
            if count == sum and not node.left and not node.right:
                ans.append(List + [node.val])
                return
            
            dfs(node.left, count, List + [node.val])
            dfs(node.right, count, List + [node.val])
        
        dfs(root, 0, [])
        return ans
