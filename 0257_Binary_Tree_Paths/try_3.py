# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [f"{root.val}"]
            
            ret = []
            left_ret = dfs(root.left)
            right_ret = dfs(root.right)

            for string in left_ret:
                ret.append(f"{root.val}->" + string)
            
            for string in right_ret:
                ret.append(f"{root.val}->" + string)
            return ret
        
        return dfs(root)
