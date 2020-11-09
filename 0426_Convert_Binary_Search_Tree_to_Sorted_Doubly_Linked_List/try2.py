"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        '''
        inorder traversal
        '''
        
        if not root:
            return
        
        head = tmp = Node(root.val)
        nodes = []
        
        def inorder(node):
            nonlocal head, tmp
            
            if not node:
                return
            
            inorder(node.left)
            
            print(node.val)
            n = Node(node.val)
            tmp.right = n
            head.left = n
            n.left = tmp
            n.right = head
            tmp = tmp.right
        
            inorder(node.right)
        
        inorder(root)
        
        tmp.right = head.right
        head.right.left = tmp
        
        return head.right