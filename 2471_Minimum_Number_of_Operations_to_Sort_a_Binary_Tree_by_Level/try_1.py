# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        que = [root]
        while que:
            vals = []
            next_que = []
            for node in que:
                vals.append(node.val)
                if node.left:
                    next_que.append(node.left)
                if node.right:
                    next_que.append(node.right)
            
            sorted_vals = sorted(vals)
            indices = {v: i for i, v in enumerate(vals)}
            
            
            for i in range(len(vals)):
                if sorted_vals[i] != vals[i]:
                    ans += 1
                    j = indices[sorted_vals[i]]
                    vals[i], vals[j] = vals[j], vals[i]
                    indices[vals[i]] = i
                    indices[vals[j]] = j
            que = next_que
            
        return ans
