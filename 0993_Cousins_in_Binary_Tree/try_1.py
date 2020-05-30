# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        limitLayer = float('inf')
        foundx = foundy = flag = False
        ans = False
        
        def dfs(node, layer = 0):
            nonlocal foundx, foundy, flag, ans, limitLayer
            if not node:
                return
            
            if not foundx and node.val == x:
                foundx = True
                if foundy  == False:
                    limitLayer = layer
            
            if not foundy and node.val == y:
                foundy = True
                if foundx == False:
                    limitLayer = layer
            
            if flag or (foundx and foundy):
                if not flag and layer == limitLayer:
                    ans = True
                return
            
            if layer+1 <= limitLayer:
                if node and node.left and node.right and \
                ((node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x)):
                    foundx = foundy = True
                    ans = False
                    flag = True
                    return
                dfs(node.left, layer+1)
                dfs(node.right, layer+1)
        
        dfs(root)
        return ans
