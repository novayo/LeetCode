# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        top-down to find all possiabilities
        '''
        def join_dict(a, b):
            for k, v in a.items():
                b[k] = b.get(k, 0) + v
            return b
        
        ans = 0
        
        def recr(node):
            nonlocal ans
            
            if not node:
                return {}
            
            if node.val == targetSum:
                ans += 1

            ret = collections.defaultdict(int)
            ret[node.val] += 1
            children = join_dict(recr(node.left), recr(node.right))
            for k, v in children.items():
                if k + node.val == targetSum:
                    ans += v
                ret[k + node.val] += v
            return ret    
        
        recr(root)
        return ans
