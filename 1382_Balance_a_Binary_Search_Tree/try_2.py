# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node, container):
            if not node:
                return
            
            inorder(node.left, container)
            container.append(node.val)
            inorder(node.right, container)
        
        tree_list = []
        inorder(root, tree_list)
        
        def build(left, right):
            
            if left > right:
                return None
            
            middle = right - (right - left) // 2
            root = TreeNode(tree_list[middle])
            root.left = build(left, middle-1)
            root.right = build(middle+1, right)
            
            return root
        
        return build(0, len(tree_list)-1)
