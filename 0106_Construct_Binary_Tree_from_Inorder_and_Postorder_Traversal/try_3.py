# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_postorder = len(postorder)-1
        index_map_inorder = {}
        for i in range(len(inorder)):
            index_map_inorder[inorder[i]] = i
        
        def recr(left, right):
            nonlocal index_postorder
            if left > right:
                return None
            
            target = postorder[index_postorder]
            root = TreeNode(target)
            
            index_inorder = index_map_inorder[target]
            index_postorder -= 1
            
            root.right = recr(index_inorder+1, right)
            root.left = recr(left, index_inorder-1)
            
            return root
        
        return recr(0, len(postorder)-1)