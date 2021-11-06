# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        # next_big => monotonic stack
        next_big_index = {}
        stack = []
        for i in range(len(preorder)):
            while stack and stack[-1] < preorder[i]:
                value = stack.pop()
                next_big_index[value] = i
            stack.append(preorder[i])
        
        while stack:
            next_big_index[stack.pop()] = len(preorder)
        
        index_preorder = 0
        def recr(i, j):
            nonlocal index_preorder
            
            if i > j:
                return
            
            root = TreeNode(preorder[index_preorder])
            index_preorder += 1
            
            if i == j:
                return root
            
            next_big = next_big_index[preorder[index_preorder-1]]
            root.left = recr(index_preorder, next_big-1)
            root.right = recr(next_big, j)
            return root
        
        return recr(0, len(preorder)-1)