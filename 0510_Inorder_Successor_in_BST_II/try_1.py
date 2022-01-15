"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        '''
        parent => less or greater than me
            => greater => might be answer
            => less => go to parent => if hit root => find root right left
        
        right => might be answer => find right left
        '''
        val = node.val
        
        if node.right:
            node = node.right
            while node.left:
                node = node.left
        else:
            while node.parent and node.parent.val < val:
                node = node.parent
            if node.parent:
                node = node.parent
            
            if node.val <= val:
                if node.right:
                    node = node.right
                    while node.left:
                        node = node.left
        
        return node if node.val > val else None
