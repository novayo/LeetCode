# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        found = collections.defaultdict(int)
        ans = []
        
        def dfs(node):
            nonlocal ans, found
            
            if not node:
                return '#'
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            string = str(node.val) + '|' + left + '|' + right
            
            if found[string] == 1:
                ans.append(node)
            found[string] += 1
            return string
            
            
        dfs(root)
        return ans
            