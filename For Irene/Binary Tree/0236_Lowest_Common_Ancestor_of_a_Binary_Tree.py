# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = None
        
        def dfs(node):
            nonlocal ans
            if ans != None:
                return -1
            
            if not node:
                return 0
            
            cur_sum = 0
            # check this node
            if node.val == p.val or node.val == q.val:
                cur_sum += 1
            
            cur_sum += dfs(node.left)
            cur_sum += dfs(node.right)
            
            if cur_sum == 2:
                ans = node
                return -1
            
            return cur_sum
        
        dfs(root)
        return ans
