# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # preorder morris traversal
        
        result = []
        
        while root:            
            if not root.left:
                result.append(root.val) # 每次都先拜訪點
                root = root.right
            else:
                # find predecessor
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    predecessor.right = root
                    result.append(root.val) # 每次都先拜訪點
                    root = root.left
                else:
                    predecessor.right = None
                    root = root.right
        
        return result
        