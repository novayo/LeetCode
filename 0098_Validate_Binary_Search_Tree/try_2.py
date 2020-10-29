# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def inorder(root, list=[]):
            if not root:
                return True


            if not inorder(root.left, list):
                return False


            if list and list[-1] >= root.val:
                return False
            else:
                list.append(root.val)


            if not inorder(root.right, list):
                return False

            return True
        
        return inorder(root, [])
