# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        cache_ans = set()
        cache = set()
        
        
        def recr(node):
            if not node:
                return ''
            
            left = recr(node.left)
            right = recr(node.right)
            cur = f'{node.val}|L|{left}|R|{right}'
            
            if cur in cache and cur not in cache_ans:
                ans.append(node)
                cache_ans.add(cur)
            
            cache.add(cur)
            return cur
        
        recr(root)
        return ans
            
