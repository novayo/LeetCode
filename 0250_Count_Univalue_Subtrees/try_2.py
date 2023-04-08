# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        '''
        左右兩邊都與自己相同（或左右子樹不存在），自己才要加入答案（才算是subtree的一員）
        '''
        ans = 0
        
        def bottom_up(node, parentVal):
            nonlocal ans
            
            if not node:
                return True
            
            left = bottom_up(node.left, node.val)
            right = bottom_up(node.right, node.val)
            if left == False or right == False:
                return False
            
            ans += 1
            return node.val == parentVal
        
        bottom_up(root, 0)
        return ans
