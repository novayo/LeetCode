# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        table = {}
        stack = []
        for i, v in enumerate(preorder):
            if v not in table:
                table[v] = len(preorder)
                
            while stack and stack[-1] < v:
                table[stack[-1]] = i
                stack.pop()
            stack.append(v)
        
        
        index_preorder = 0
        def build(i, j):
            nonlocal index_preorder
            if i > j:
                return None
            
            root = TreeNode(preorder[index_preorder])
            index_preorder += 1
            
            if i == j:
                return root
            
            index_bigger = table[preorder[index_preorder-1]]
            root.left = build(i+1, index_bigger-1)
            root.right = build(index_bigger, j)
            return root
        
        return build(0, len(preorder)-1)
