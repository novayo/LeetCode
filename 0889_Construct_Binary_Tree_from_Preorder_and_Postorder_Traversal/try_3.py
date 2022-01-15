# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        table = {}
        for i in range(len(postorder)):
            table[postorder[i]] = i
        
        index_preorder = 0
        def build(i, j):
            nonlocal index_preorder
            if i > j:
                return None
            
            root = TreeNode(preorder[index_preorder])
            index_preorder += 1
            
            if i == j:
                return root
            
            index_postorder = table[preorder[index_preorder]]
            root.left = build(i, index_postorder)
            root.right = build(index_postorder+1, j-1)
            return root
        
        return build(0, len(preorder)-1)
