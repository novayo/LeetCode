# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def recr(node, curPath):
            if not node:
                return
            
            if not curPath:
                curPath = f"{node.val}"
            else:
                curPath += f"->{node.val}"
            
            if not node.left and not node.right:
                ans.append(curPath)
            
            recr(node.left, curPath)
            recr(node.right, curPath)
        
        recr(root, "")
        return ans
