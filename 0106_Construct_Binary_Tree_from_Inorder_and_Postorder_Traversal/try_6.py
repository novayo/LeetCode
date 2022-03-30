# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_inorder = {}
        for i, v in enumerate(inorder):
            index_inorder[v] = i
        
        
        index_of_postorder = len(postorder)-1
        def recr(l, r):
            nonlocal index_of_postorder
            if l > r:
                return None
            
            root = TreeNode(postorder[index_of_postorder])
            index_of_postorder -= 1
            
            if l == r:
                return root
            
            index = index_inorder[root.val]
            root.right = recr(index+1, r)
            root.left = recr(l, index-1)
            return root
        
        return recr(0, len(postorder)-1)
            