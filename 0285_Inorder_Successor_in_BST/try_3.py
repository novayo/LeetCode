# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        bigger = []
        
        while root:
            if root.val == p.val:
                if root.right:
                    root = root.right
                    while root.left:
                        root = root.left
                    return root
                elif bigger:
                    return bigger[-1]
                else:
                    break
            elif root.val > p.val:
                bigger.append(root)
                root = root.left
            else:
                root = root.right
        
        return None