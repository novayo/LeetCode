# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        '''
        先找最左邊 => 得知深度
        在找右邊 => 第一個hit return
        '''
        def findLeftDepth(root):
            node = root
            high = 0
            while node:
                high += 1
                node = node.left
            return high
        
        if not root:
            return 0
        
        left_depth = findLeftDepth(root.left)
        right_depth = findLeftDepth(root.right)
        
        if left_depth == right_depth:
            left = 2**left_depth - 1
            right = self.countNodes(root.right)
            return left + right + 1
        else:
            right = 2**right_depth - 1
            left = self.countNodes(root.left)
            return left + right + 1
        
