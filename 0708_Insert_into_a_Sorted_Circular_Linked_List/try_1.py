"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        '''
        lower -> {insert} -> upper
        
        if find high -> low
            => if insert > high => insert
            => if insert < low => insert
        '''
        
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        if head == head.next:
            head.next = Node(insertVal)
            head.next.next = head
            return head
        
        lower = head
        upper = head.next
        stop = lower
        while upper != stop:
            if lower.val > upper.val:
                if insertVal >= lower.val or insertVal <= upper.val:
                    break
            else:
                if lower.val <= insertVal <= upper.val:                    
                    break
            
            lower, upper = lower.next, upper.next
        
        lower.next = Node(insertVal)
        lower.next.next = upper
        
        return head