# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            node, curSum = queue.popleft()

            if node is None:
                continue

            curSum += node.val
            if node.left is None and node.right is None:
                if curSum == targetSum:
                    return True
            else:
                queue.append((node.left, curSum))
                queue.append((node.right, curSum))

        return False
