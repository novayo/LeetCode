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
        if not root or not root.left:
            return root
        
        queue = collections.deque()
        queue.append((root, 0))
        
        left = None
        lLevel = -1
        while queue:
            right, rLevel = queue.popleft()
            
            if rLevel == lLevel:
                left.next = right
            
            left = right
            lLevel = rLevel
            
            if left.left:
                queue.append((left.left, lLevel+1))
                queue.append((left.right, lLevel+1))
        return root