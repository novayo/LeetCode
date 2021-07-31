# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        '''
        對每個node來說，區分遞增遞減的數值
        每個點區計算一次左右值的可能性並紀錄當前最大
        '''
        ans = 1
        
        def dfs(node):
            nonlocal ans
            
            if not node.left and not node.right:
                return 1, 1
            
            l_val = r_val = -float(inf)
            l_inc = l_dec = r_inc = r_dec = 0
            if node.left:
                l_val = node.left.val
                l_inc, l_dec = dfs(node.left)
            if node.right:
                r_val = node.right.val
                r_inc, r_dec = dfs(node.right)
            
            inc = dec = 0
            if abs(node.val - l_val) == 1:
                if node.val > l_val:
                    dec = max(dec, l_dec) # 可能會兩邊都比此點小，則要選出最長邊
                else:
                    inc = max(inc, l_inc)
            
            if abs(node.val - r_val) == 1:
                if node.val > r_val:
                    dec = max(dec, r_dec)
                else:
                    inc = max(inc, r_inc)
            
            ans = max(ans, inc + dec + 1)
            return inc+1, dec+1
        
        dfs(root)
        return ans
