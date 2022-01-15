# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        table = {}
        for i, v in enumerate(inorder):
            table[v] = i
        
        index_postorder = len(postorder)-1
        def build(i, j):
            nonlocal index_postorder
            
            if i > j:
                return None
            
            root = TreeNode(postorder[index_postorder])
            index_postorder -= 1
            
            if i == j:
                return root
            
            index_inorder = table[postorder[index_postorder+1]]
            root.right = build(index_inorder+1, j)
            root.left = build(i, index_inorder-1)
            return root
        
        return build(0, len(postorder)-1)
