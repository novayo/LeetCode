# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.recursion(root, ans)
        # self.iteration(root, ans)
        # self.morris(root, ans)
        return ans
        
    def recursion(self, node, result):
        if not node:
            return

        result.append(node.val)
        self.recr(node.left, result)
        self.recr(node.right, result)
        
    def iteration(self, node, result):
        if not node:
            return
        
        stack = []
        while node or stack:
            if node:
                stack.append(node)
                result.append(node.val)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
    
    def morris(self, node, result):
        if not node:
            return
        
        while node:
            if not node.left:
                result.append(node.val)
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                
                if not predecessor.right:
                    predecessor.right = node
                    result.append(node.val)
                    node = node.left
                else:
                    predecessor.right = None
                    node = node.right