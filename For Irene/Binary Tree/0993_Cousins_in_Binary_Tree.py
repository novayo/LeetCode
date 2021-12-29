# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        if not root:
            return False
        
        if root.val == x or root.val == y:
            return False
        
        
        # x_info, y_info = self.bfs(root, x, y)
        x_info, y_info = self.dfs(root, x, y)
        
        
        if x_info[0] != y_info[0] and x_info[1] == y_info[1]:
            return True
        else:
            return False
    
    def dfs(self, root, x, y):
        x_info = [] # [parent.value, layer]
        y_info = [] # [parent.value, layer]
        
        def _dfs(node, layer):
            nonlocal x_info, y_info
            
            if not node:
                return
            
            
            if node.left:
                if node.left.val == x:
                    x_info = [node.val, layer+1]
                
                if node.left.val == y:
                    y_info = [node.val, layer+1]
            
            if node.right:
                if node.right.val == x:
                    x_info = [node.val, layer+1]
                
                if node.right.val == y:
                    y_info = [node.val, layer+1]
            
            _dfs(node.left, layer+1)
            _dfs(node.right, layer+1)
        
        
        _dfs(root, 0)
        return x_info, y_info
        
    
    
    def bfs(self, root, x, y):
        x_info = [] # [parent.value, layer]
        y_info = [] # [parent.value, layer]
        
        queue = collections.deque()
        queue.appendleft((root, 0))
        
        # bfs
        while queue:
            node, layer = queue.pop()
            
            if node.left:
            
                queue.appendleft((node.left, layer+1))
            
                if node.left.val == x:
                    x_info = [node.val, layer+1]
                
                if node.left.val == y:
                    y_info = [node.val, layer+1]
            
            if node.right:
                
                queue.appendleft((node.right, layer+1))
                
                if node.right.val == x:
                    x_info = [node.val, layer+1]
            
                if node.right.val == y:
                    y_info = [node.val, layer+1]
        
        return x_info, y_info
        