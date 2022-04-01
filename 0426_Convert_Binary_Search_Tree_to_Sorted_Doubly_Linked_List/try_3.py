"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        pre = dummy = Node(-1)
        def dfs(node):
            def _dfs(node):
                nonlocal pre, dummy
                if not node:
                    return
                _dfs(node.left)
                pre.right = node
                node.left = pre
                pre = node
                _dfs(node.right)
            
            _dfs(node)
            pre.right = dummy.right
            dummy.right.left = pre
        
        def iteration(node):
            nonlocal pre, dummy
            
            stack = []
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    
                    pre.right = node
                    node.left = pre
                    pre = node
                    
                    node = node.right
            
            pre.right = dummy.right
            dummy.right.left = pre
            
        def morris(node):
            nonlocal pre, dummy
            
            while node:
                if not node.left:
                    pre.right = node
                    node.left = pre
                    pre = node
                    
                    node = node.right
                else:
                    p = node.left
                    while p.right and p.right != node:
                        p = p.right
                    
                    if p.right != node:
                        p.right = node
                        node = node.left
                    else:
                        p.right = None
                        
                        pre.right = node
                        node.left = pre
                        pre = node
                        
                        node = node.right
                        
            pre.right = dummy.right
            dummy.right.left = pre
                    
        
        # dfs(root)
        # iteration(root)
        morris(root)
        
        return dummy.right