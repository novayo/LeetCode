# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        while root:
            if not root.left:
                result.append(root.val)
                root = root.right
            else:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    predecessor.right = root
                    root = root.left
                else:
                    predecessor.right = None
                    result.append(root.val)
                    root = root.right
        
        return result
