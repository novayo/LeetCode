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
        
        head = tmp = Node(-1)
        nodes = []
        
        def inorder(node, nodes):
            if not node:
                return
            
            inorder(node.left, nodes)
            
            nodes.append(node.val)
            
            inorder(node.right, nodes)
        
        inorder(root, nodes)
        
        for v in nodes:
            node = Node(v)
            tmp.right = node
            node.left = tmp
            tmp = node
        
        tmp.right = head.right
        head.right.left = tmp
        
        return head.right