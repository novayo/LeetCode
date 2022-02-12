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
        if not root:
            return root
        
        # bfs
        queue = [root]
                
        while queue:
            next_queue = []
            
            for i in range(1, len(queue)):
                queue[i-1].next = queue[i]
                if queue[i-1].left:
                    next_queue.append(queue[i-1].left)
                if queue[i-1].right:
                    next_queue.append(queue[i-1].right)
            
            queue[-1].next = None
            if queue[-1].left:
                next_queue.append(queue[-1].left)
            if queue[-1].right:
                next_queue.append(queue[-1].right)
            queue = next_queue
        
        return root
