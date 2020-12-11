# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        '''
        bottom up with hash set
        '''     
        seen = collections.defaultdict(int)
        ans = []
        
        def bottom_up(node):
            if not node:
                return '#'
            
            tmp = [node.val]
            for n in bottom_up(node.left):
                tmp.append(n)
            
            for n in bottom_up(node.right):
                tmp.append(n)
            
            t = tuple(tmp)
            if seen[t] == 1:
                ans.append(node)
            seen[t] += 1
            return tmp
        
        bottom_up(root)
        return ans

