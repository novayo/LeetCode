# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get(node):
            return node.val if node else None
        
        
        if not (root1 and root2):
            return (not root1 and not root2)
        
        if root1.val != root2.val:
            return False
        
        queue = collections.deque()
        queue.appendleft((root1, root2))
        
        while queue:
            node1, node2 = queue.pop()
            
            if not node1 and not node2:
                continue
            
            if get(node1.left) == get(node2.left) and get(node1.right) == get(node2.right):
                queue.appendleft((node1.left, node2.left))
                queue.appendleft((node1.right, node2.right))
            
            elif get(node1.left) == get(node2.right) and get(node1.right) == get(node2.left):
                queue.appendleft((node1.left, node2.right))
                queue.appendleft((node1.right, node2.left))
            
            else:
                return False
        
        return True
            
