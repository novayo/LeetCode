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
    def flatten(self, head: 'Node') -> 'Node':
        # dfs
        curNode = ret = Node(-1)
        
        def dfs(node):
            nonlocal curNode
            
            if not node:
                return
            
            curNode.next = Node(node.val)
            curNode.next.prev = curNode
            curNode = curNode.next
            
            # 先去紀錄child
            dfs(node.child)
            
            # 再去往後紀錄
            dfs(node.next)
        
        dfs(head)
        if ret.next:
            ret.next.prev = None
        return ret.next
