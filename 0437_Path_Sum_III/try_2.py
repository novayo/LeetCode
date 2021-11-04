# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        LC560 => presum + hash table => O(n)
        '''
        
        d = collections.defaultdict(int)
        d[0] = 1 # presum = target時也需要+1
        
        def recr(node, curSum):
            nonlocal ans
            
            if not node:
                return
            
            # presum
            curSum += node.val
            ans += d[curSum - targetSum]
            
            # backtracking
            d[curSum] += 1
            
            recr(node.left, curSum)
            recr(node.right, curSum)
            
            d[curSum] -= 1
        
        ans = 0
        recr(root, 0)
        return ans
