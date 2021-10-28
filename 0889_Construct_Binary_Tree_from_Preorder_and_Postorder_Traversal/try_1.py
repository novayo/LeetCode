# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_pre = index_post = 0
        
        def recr():
            nonlocal index_pre, index_post
            root = TreeNode(preorder[index_pre])
            index_pre += 1
            
            if root.val != postorder[index_post]:
                root.left = recr()
            
            if root.val != postorder[index_post]:
                root.right = recr()
            
            index_post += 1
            return root
        
        return recr()