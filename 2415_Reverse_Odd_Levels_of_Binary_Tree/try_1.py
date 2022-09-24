# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        level = 0
        queue = [root]
        
        while queue:
            next_queue = []
            
            if level % 2 == 1:
                vals = [node.val for node in queue]
                for node in queue:
                    node.val = vals.pop()
            
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
                    
            queue = next_queue
            level += 1
            
        return root
