# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''
        先找最左邊 => 得知深度
        在找右邊 => 第一個hit return
        '''
        if not root:
            return 0
        
        high = 1
        
        tmp = root
        while tmp.left:
            high += 1
            tmp = tmp.left
        
        
        ans = None
        def dfs(node, num=1, layer=1):
            nonlocal ans
            if ans:
                return
            
            if not node:
                return
            
            if layer == high:
                ans = num
                return
            
            dfs(node.right, num*2+1, layer+1)
            dfs(node.left, num*2, layer+1)
        
        dfs(root)
        return ans
        
        
        
