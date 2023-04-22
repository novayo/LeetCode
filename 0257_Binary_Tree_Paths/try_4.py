# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        queue = collections.deque()
        queue.append((root, ""))

        while queue:
            node, curPath = queue.popleft()

            if node is None:
                continue

            if curPath == '':
                curPath = f'{node.val}'
            else:
                curPath += f'->{node.val}'

            if node.left is None and node.right is None:
                ans.append(curPath)

            queue.append((node.left, curPath))
            queue.append((node.right, curPath))

        return ans
