# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # bfs
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        if root.left.val != root.right.val:
            return False
        
        queue = collections.deque()
        queue.append((root.left, root.right))
        
        while queue:
            leftNode, rightNode = queue.popleft()
            
            if not leftNode and not rightNode:
                continue
            
            if not leftNode or not rightNode:
                return False
            
            if leftNode.val != rightNode.val:
                return False
            
            queue.append((leftNode.left, rightNode.right))
            queue.append((leftNode.right, rightNode.left))
            
        return True
