# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level = 0
        max_val = -float('inf')

        queue = collections.deque()
        queue.append(root)
        cur_level = 0

        while queue:
            next_layer = collections.deque()
            cur_level += 1

            curSum = 0
            for node in queue:
                if node is None:
                    continue
                curSum += node.val
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)

            if curSum > max_val:
                max_val = curSum
                max_level = cur_level

            queue = next_layer

        return max_level
