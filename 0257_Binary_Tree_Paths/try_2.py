# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        curPath = ""
        
        stack = []        
        while root or stack:
            if root:
                # visit
                if curPath == "":
                    curPath = f"{root.val}"
                else:
                    curPath = curPath + f"->{root.val}"
                if root.left is None and root.right is None:
                    ans.append(curPath)
                
                stack.append((root, curPath))
                root = root.left
            else:
                root, curPath = stack.pop()
                root = root.right
        return ans
