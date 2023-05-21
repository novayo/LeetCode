# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findSuccessor(node):
            while node and node.left:
                node = node.left
            return node.val
        
        def findPredecessor(node):
            while node and node.right:
                node = node.right
            return node.val
        
        def delete(node, target):
            if not node:
                return node
            
            if node.val < target:
                node.right = delete(node.right, target)
            elif node.val > target:
                node.left = delete(node.left, target)
            else:
                if not node.left and not node.right:
                    node = None
                elif node.right:
                    successor = findSuccessor(node.right)
                    node.val = successor
                    node.right = delete(node.right, successor)
                else:
                    predecessor = findPredecessor(node.left)
                    node.val = predecessor
                    node.left = delete(node.left, predecessor)
            return node
        
        return delete(root, key)
            
