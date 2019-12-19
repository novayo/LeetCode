# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = collections.deque()
        pre = -float('inf')
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack: break
            tmp = stack.pop()
            if pre == p.val:
                return tmp
            pre = tmp.val
            root = tmp.right
            
        return None
