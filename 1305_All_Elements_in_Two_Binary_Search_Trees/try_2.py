# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1 = []
        stack2 = []
        ans = []
        
        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            
            while root2:
                stack2.append(root2)
                root2 = root2.left
        
            if stack1 and stack2:
                if stack1[-1].val <= stack2[-1].val:
                    node = stack1.pop()
                    ans.append(node.val)
                    root1 = node.right
                else:
                    node = stack2.pop()
                    ans.append(node.val)
                    root2 = node.right
            elif stack1:
                node = stack1.pop()
                ans.append(node.val)
                root1 = node.right
            elif stack2:
                node = stack2.pop()
                ans.append(node.val)
                root2 = node.right
        
        return ans