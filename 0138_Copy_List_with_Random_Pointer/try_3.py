"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        change val if we visited
        if not visited yet => do dfs
        '''
        if not head:
            return head
        
        found = {head: Node(head.val)}
        def dfs(old_node):
            if not old_node:
                return
            
            new_node = found[old_node]
            if old_node.next:
                if old_node.next not in found:
                    found[old_node.next] = Node(old_node.next.val)
                    dfs(old_node.next)
                new_node.next = found[old_node.next]
            
            if old_node.random:
                if old_node.random not in found:
                    found[old_node.random] = Node(old_node.random.val)
                    dfs(old_node.random)
                new_node.random = found[old_node.random]
        
        dfs(head)
        return found[head]
