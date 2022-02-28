# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        stack = [root]
        
        while stack:
            ans.append([])
            next_layer = []
            
            for node in stack:
                ans[-1].append(node.val)
                
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            stack = next_layer
        return ans
