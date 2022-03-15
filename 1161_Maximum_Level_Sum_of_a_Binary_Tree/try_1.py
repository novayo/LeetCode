# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # level order traversal
        max_sum = -float('inf')
        min_layer = 0
        
        container = [root]
        layer = 1
        while container:
            next_container = []
            
            _sum = 0
            for node in container:
                _sum += node.val
                if node.left:
                    next_container.append(node.left)
                if node.right:
                    next_container.append(node.right)
            
            if _sum > max_sum:
                max_sum = _sum
                min_layer = layer
            
            layer += 1
            container = next_container
        
        return min_layer