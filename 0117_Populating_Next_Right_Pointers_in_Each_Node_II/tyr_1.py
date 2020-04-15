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
    def connect(self, root: 'Node') -> 'Node':
        layer = root
        
        while layer:
            cur = layer
            next = None
            while cur:
                if cur.left and cur.right:
                    cur.left.next = cur.right
                
                if not next:
                    next = cur.left or cur.right
                
                target = cur.right or cur.left
                
                if target:
                    tmp = cur.next
                    while tmp:
                        if tmp.left:
                            target.next = tmp.left
                            break
                        elif tmp.right:
                            target.next = tmp.right
                            break
                        tmp = tmp.next
                cur=cur.next
            layer = next
        return root
