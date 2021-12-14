# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        queue = collections.deque()
        queue.appendleft(root)
        
        while queue:
            node = queue.pop()
            
            if not node.left and not node.right:
                if node.val == targetSum:
                    return True
            else:
                if node.left:
                    node.left.val += node.val
                    queue.appendleft(node.left)
                
                if node.right:
                    node.right.val += node.val
                    queue.appendleft(node.right)
        
        return False
                
            