# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # inorder traversal
        stack = collections.deque()
        
        i = 0
        while True:
            while root:
                stack.append(root)
                root = root.left
                
            if stack == None: break
                
            node = stack.pop()
            i += 1
            if i == k:
                return node.val
            root = node.right
