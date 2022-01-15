# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        table = {}
        for i, v in enumerate(inorder):
            table[v] = i
        
        index_preorder = 0
        def build(i, j):
            nonlocal index_preorder
            if i > j:
                return None
            
            root = TreeNode(preorder[index_preorder])
            index_preorder += 1
            
            if i == j:
                return root
            
            index_inorder = table[preorder[index_preorder-1]]
            root.left = build(i, index_inorder-1)
            root.right = build(index_inorder+1, j)
            return root
        
        return build(0, len(preorder)-1)
