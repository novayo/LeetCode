# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def dfs(node, cur_path):
            nonlocal ans
            if not node.left and not node.right:
                ans.append('->'.join(cur_path+[str(node.val)]))
                return
            
            if node.left:
                dfs(node.left, cur_path+[str(node.val)])
            if node.right:
                dfs(node.right, cur_path+[str(node.val)])
        
        dfs(root, [])
        return ans
