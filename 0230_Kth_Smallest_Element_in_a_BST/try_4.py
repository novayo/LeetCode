# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # morris
        count = 0
        while root:
            if not root.left:
                count += 1
                if count >= k:
                    return root.val
                root = root.right
            else:
                node = root.left
                while node.right and node.right != root:
                    node = node.right
                
                if node.right != root:
                    node.right = root
                    root = root.left
                else:
                    node.right = None
                    count += 1
                    if count >= k:
                        return root.val
                    root = root.right

