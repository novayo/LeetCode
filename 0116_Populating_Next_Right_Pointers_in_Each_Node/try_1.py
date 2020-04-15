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
        queue = collections.deque()
        queue.append((root))
        
        pre = None
        count = 1
        while queue:
            node = queue.popleft()
            
            if not node:
                continue
            if pre:
                pre.next = node
            if count in {1,3,7,15,31,63,127,255,511,1023,2047,4095}:
                pre = None
                node.next = None
            else:
                pre = node
            queue.append(node.left)
            queue.append(node.right)
            count += 1

        return root
