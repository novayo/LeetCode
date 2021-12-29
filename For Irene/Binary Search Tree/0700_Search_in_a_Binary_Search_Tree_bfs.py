# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        queue = collections.deque()
        queue.appendleft(root)
        
        while queue:
            node = queue.pop()
            
            if not node:
                continue
            
            if node.val == val:
                return node
            
            if val < node.val:
                queue.appendleft(node.left)
            
            if val > node.val:
                queue.appendleft(node.right)
            
        return None