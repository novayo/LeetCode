# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        
        def dfs(node, count=0):
            nonlocal ans
            
            if not node:
                return
            
            if count == len(ans):
                ans.append(collections.deque([node.val]))
            else:
                if count % 2 == 1:
                    ans[count].appendleft(node.val)
                else:
                    ans[count].append(node.val)
            dfs(node.left, count+1)
            dfs(node.right, count+1)
        
        dfs(root)
        
        return ans
