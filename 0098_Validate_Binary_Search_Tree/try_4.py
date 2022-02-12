# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        return [min, max]
        
        root => check if left.max < root.val < right.min
             => return min, max of right and left
        '''
        
        ans = True
        def recr(node):
            nonlocal ans
            if ans == False:
                return float('inf'), -float('inf')
            
            if not node.left and not node.right:
                return node.val, node.val
            
            l_min = l_max = r_min = r_max = node.val
            if node.left:
                l_min, l_max = recr(node.left)
            else:
                l_max = -float('inf')
                
            if node.right:
                r_min, r_max = recr(node.right)
            else:
                r_min = float('inf')
            
            if not (l_max < node.val < r_min):
                ans = False
                return float('inf'), -float('inf')
            else:
                return l_min, r_max
        
        recr(root)
        return ans
