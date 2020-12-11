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
            
            tmp = "" + str(node.val) + "," + bottom_up(node.left) + "," + bottom_up(node.right)
            
            if seen[tmp] == 1:
                ans.append(node)
            seen[tmp] += 1
            return tmp
        
        bottom_up(root)
        return ans

