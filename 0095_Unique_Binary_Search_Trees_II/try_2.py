# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def recr(i, j):
            if i > j:
                return [None]
            
            ret = []
            for root in range(i, j+1):
                left = recr(i, root-1)
                right = recr(root+1, j)
                
                for l in left:
                    for r in right:
                        tmp = TreeNode(root)
                        tmp.left = l
                        tmp.right = r
                        ret.append(tmp)

            return ret
        
        return recr(1, n)
            
