# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        
        queue = collections.deque()
        queue.appendleft(root)
        
        while queue:
            node = queue.pop()
            
            if low <= node.val <= high:
                ans += node.val
            
            if node.left:
                queue.appendleft(node.left)
                
            if node.right:
                queue.appendleft(node.right)
        
        return ans
