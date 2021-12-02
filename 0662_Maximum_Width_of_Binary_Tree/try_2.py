# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        queue = collections.deque()
        queue.appendleft((root, 0))
        while queue:
            tmp = collections.deque()
            head = queue[-1][1]
            while queue:
                node, col_index = queue.pop()
                
                if node.left:
                    tmp.appendleft((node.left, col_index*2))
                if node.right:
                    tmp.appendleft((node.right, col_index*2+1))
            
            queue = tmp
            ans = max(ans, col_index - head + 1)
        
        return ans
