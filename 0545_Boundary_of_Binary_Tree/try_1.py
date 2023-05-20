# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
            return [root.val]

        node = root.left
        leftBounadry = []
        while node:
            leftBounadry.append(node.val)
            if node.left:
                node = node.left
            elif node.right:
                node = node.right
            else:
                leftBounadry.pop()
                break
        
        node = root.right
        rightBoundary = []
        while node:
            rightBoundary.append(node.val)
            if node.right:
                node = node.right
            elif node.left:
                node = node.left
            else:
                rightBoundary.pop()
                break
        rightBoundary.reverse()

        leaves = []
        def recr(node):
            nonlocal leaves
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            recr(node.left)
            recr(node.right)
        recr(root)

        return [root.val] + leftBounadry + leaves + rightBoundary