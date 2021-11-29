# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque()
        queue.appendleft(root)
        
        layer = 0
        while queue:
            # 每跑完一層，答案+1
            layer += 1
            next_queue = collections.deque()
            
            # 把當前這層的元素一個一個抓出來
            while queue:
                node = queue.pop()
                
                # 把下一層給存起來
                if node.left:
                    next_queue.appendleft(node.left)
                if node.right:
                    next_queue.appendleft(node.right)
            
            # 再去跑下一層
            queue = next_queue
        
        return layer
