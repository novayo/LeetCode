# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # iteration
        stack = []
        ans = collections.deque()
       
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                ans.appendleft(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                
        return ans