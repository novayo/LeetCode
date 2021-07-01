# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        ans = []
        
        def add_to_ans(target, index):
            if index >= len(ans):
                ans.append([])
            ans[index].append(target)
        
        def recr(node):
            if not node:
                return -1
            
            left = recr(node.left)
            right = recr(node.right)
            
            level = max(left, right) + 1
            
            add_to_ans(node.val, level)
            
            return level
        
        recr(root)
        return ans
        
