# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        bfs -> number the node -> calculate ans for each layer
        '''
        ans = 0
        stack = [(root, 1)]
        
        while stack:
            l, r = float('inf'), -float('inf')
            next_stack = []
            
            for node, number in stack:
                l = min(l, number)
                r = max(r, number)
                
                if node.left:
                    next_stack.append((node.left, number*2))
                if node.right:
                    next_stack.append((node.right, number*2+1))
            
            ans = max(ans, r-l+1)
            stack = next_stack
        
        return ans        
            