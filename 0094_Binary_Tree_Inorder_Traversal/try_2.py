# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # bfs
        ans = collections.deque() 
        queue = collections.deque()
        
        while True:
            while root:
                queue.append(root)
                root = root.left

            if not queue:
                break
            
            root = queue.pop()
            ans.append(root.val)
            root = root.right
        
        return ans
