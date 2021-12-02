# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        ans = []
        queue = collections.deque()
        queue.appendleft((None, root, 0))
        while queue:
            parent, node, layer = queue.pop()

            if node.val in [x, y]:
                ans.append((parent, layer))

                if len(ans) >= 2:
                    break
                    
            if node.left:
                queue.appendleft((node, node.left, layer+1))
            if node.right:
                queue.appendleft((node, node.right, layer+1))
        
        if len(ans)!=2:
            return False
        
        if ans[0][0] != ans[1][0] and ans[0][1] == ans[1][1]:
            return True
        else:
            return False
                
                
                
