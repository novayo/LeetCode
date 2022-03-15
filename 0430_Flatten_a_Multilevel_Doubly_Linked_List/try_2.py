"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        tmp = dummy = Node()
        
        stack = [head]
        while stack:
            node = stack.pop()
            
            tmp.next = Node(node.val, tmp)
            tmp = tmp.next
            
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
        
        ret = dummy.next
        ret.prev = None
        return ret
        