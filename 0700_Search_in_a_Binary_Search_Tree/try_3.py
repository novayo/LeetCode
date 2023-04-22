# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node is None:
                continue

            if node.val == val:
                return node

            queue.append(node.left)
            queue.append(node.right)

        return None
