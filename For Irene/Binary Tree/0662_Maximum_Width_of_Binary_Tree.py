# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ans = 0
        
        queue = collections.deque()
        queue.appendleft((root, 1))
        
        while queue:
            
            next_queue = collections.deque()
            
            cur_min, cur_max = float('inf'), -float('inf')
            while queue:
                node, number = queue.pop()
                
                # min max number of this layer
                cur_min = min(cur_min, number)
                cur_max = max(cur_max, number)
                
                # push next layer
                if node.left:
                    next_queue.appendleft((node.left, number*2))
                
                if node.right:
                    next_queue.appendleft((node.right, number*2+1))
            
            ans = max(ans, cur_max-cur_min+1)
            queue = next_queue
        
        return ans