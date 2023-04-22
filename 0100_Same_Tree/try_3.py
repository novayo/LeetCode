# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(root):
            ans = []
            queue = collections.deque()
            queue.append(root)

            while queue:
                node = queue.popleft()

                ans.append(node.val if node else None)
                if node is None:
                    continue
                queue.append(node.left)
                queue.append(node.right)

            return ans

        return bfs(p) == bfs(q)
