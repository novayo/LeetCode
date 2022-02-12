# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursion
        def inorder(node, container):
            if not node:
                return
            
            if len(container) >= k:
                return
            
            inorder(node.left, container)
            container.append(node.val)
            inorder(node.right, container)
        
        ans = []
        inorder(root, ans)
        return ans[k-1]
