# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        ans = 0
        
        def recr(node):
            nonlocal ans
            if not node:
                return {}
            
            left_set = recr(node.left)
            right_set = recr(node.right)
            
            target = targetSum - node.val
            
            if node.val == targetSum:
                ans += 1
            
            if target in left_set:
                ans += left_set[target]
            
            if target in right_set:
                ans += right_set[target]
                
            tmp = {}
            for v in left_set:
                o = left_set[v]
                _o = tmp.get(v + node.val, 0)
                tmp[v + node.val] = o + _o
            
            for v in right_set:
                o = right_set[v]
                _o = tmp.get(v + node.val, 0)
                tmp[v + node.val] = o + _o
            
            tmp[node.val] = tmp.get(node.val, 0) + 1
            
            return tmp
        
        recr(root)
        return ans
