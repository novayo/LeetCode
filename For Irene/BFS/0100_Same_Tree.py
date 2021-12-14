# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        p = [1,2,None]
        q = [1,None,2]
        '''
        
        def bfs(root):
            ans = []
            
            queue = collections.deque()
            queue.appendleft(root)
            
            while queue:
                node = queue.pop()
                
                if node == None:
                    ans.append(None)
                    continue
                else:
                    ans.append(node.val)
        
                queue.appendleft(node.left)
                queue.appendleft(node.right)
            
            return ans
        
        p_list = bfs(p)
        q_list = bfs(q)
        
        for _p, _q in zip(p_list, q_list):
            if _p != _q:
                return False
        
        return True
        