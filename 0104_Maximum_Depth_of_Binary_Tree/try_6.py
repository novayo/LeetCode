# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            node, curDepth = queue.popleft()

            if node is None:
                continue

            curDepth += 1
            ans = max(ans, curDepth)
            queue.append((node.left, curDepth))
            queue.append((node.right, curDepth))

        return ans
