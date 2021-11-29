# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        
        while queue:
            node_l = queue.pop()
            node_r = queue.pop()
            
            if node_l == None and node_r == None:
                continue
            elif node_l == None and node_r != None:
                return False
            elif node_r == None and node_l != None:
                return False
            
            if node_l.val != node_r.val:
                return False
            
            queue.appendleft(node_l.left)
            queue.appendleft(node_r.right)
            
            queue.appendleft(node_l.right)
            queue.appendleft(node_r.left)
        
        return True
