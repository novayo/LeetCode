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
            
            ans = []
            for k in range(i, j+1):
                left_subtree = recr(i, k-1)
                right_subtree = recr(k+1, j)

                for l in left_subtree:
                    for r in right_subtree:
                        root = TreeNode(k)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans
        
        return recr(1, n)
