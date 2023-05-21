# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        def recr(node):
            if not node:
                return None
    
            if node.val == p.val:
                if node.right:
                    n = node.right
                    while n and n.left:
                        n = n.left
                    return n
                else:
                    return None
            elif node.val < p.val:
                n = recr(node.right)
                return n
            else:
                n = recr(node.left)
                return n if n else node
        
        return recr(root)
