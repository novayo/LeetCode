# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def preorder(node, cur_list):
            if not node:
                cur_list.append(None)
                return
            
            cur_list.append(node.val)
            preorder(node.left, cur_list)
            preorder(node.right, cur_list)
        
        p_list = []
        preorder(p, p_list)
        
        q_list = []
        preorder(q, q_list)
        
        for i in range(len(p_list)):
            _p = p_list[i]
            _q = q_list[i]
            
            if _p != _q:
                return False
            
        return True
        
            
            
