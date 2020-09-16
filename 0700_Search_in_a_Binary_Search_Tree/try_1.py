# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        '''
        subroutine：val大，走右邊;val較小，走左邊
        base：
            * 找到：去check回傳回來是否有東西，有就繼續return
            * 沒找到：不用理
        '''
        
        def recr(node):
            # base
            if not node:
                return None
            
            # subroutine
            if val > node.val:
                ret = recr(node.right)
                if ret:
                    return ret
            elif val == node.val:
                return node
            else:
                ret = recr(node.left)
                if ret:
                    return ret
        
        return recr(root)
