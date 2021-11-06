# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        index = {}
        for i in range(len(postorder)):
            index[postorder[i]] = i
        
        index_preorder = 0
        def recr(i, j):
            nonlocal index_preorder
            
            if i > j:
                return
            
            root = TreeNode(preorder[index_preorder])
            index_preorder += 1
            
            if i == j:
                return root
            
            next_preorder = preorder[index_preorder]
            root.left  = recr(i, index[next_preorder])
            root.right = recr(index[next_preorder]+1, j-1)
            
            return root
        
        return recr(0, len(postorder)-1)