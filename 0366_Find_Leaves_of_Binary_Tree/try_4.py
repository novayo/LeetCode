# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def recr(node):
            if not node:
                return []
            
            ret = []
            left = recr(node.left)
            right = recr(node.right)
            
            for i in range(max(len(left), len(right))):
                tmp = []
                if i < len(left):
                    tmp += left[i]
                
                if i < len(right):
                    tmp += right[i]
                
                ret.append(tmp)
            
            return ret + [[node.val]]
        
        return recr(root)
            
