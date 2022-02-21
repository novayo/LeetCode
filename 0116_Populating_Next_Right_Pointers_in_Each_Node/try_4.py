"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        記住最左邊的值，每次都跑一整層
        '''
        if not root:
            return root
        
        leftmost = root
        
        while leftmost.left:
            head = leftmost
            
            while head:
                head.left.next = head.right
                
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            
            leftmost = leftmost.left
        
        return root
        
        