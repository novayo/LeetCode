# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0
        
        def recr(node):
            nonlocal ans
            
            if not node:
                return {}
            if not node.left and not node.right:
                return {1:1}
            
            left = recr(node.left)
            right = recr(node.right)
            
            sort_left = sorted(left.keys())
            sort_right = sorted(right.keys())
            
            # O(100)
            for l in sort_left:
                for r in sort_right:
                    if l + r > distance:
                        break
                    ans += left[l] * right[r]
            
            ret = collections.defaultdict(int)
            # O(10)
            for key in sort_left:
                if key+1 < distance:
                    ret[key+1] += left[key]
            for key in sort_right:
                if key+1 < distance:
                    ret[key+1] += right[key]
            return ret
        
        recr(root)
        return ans