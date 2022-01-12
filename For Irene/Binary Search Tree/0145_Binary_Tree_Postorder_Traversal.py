# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.recursion(root, ans)
        # self.iteration(root, ans)
        # self.morris(root, ans)
        return ans
    
    def recursion(self, node, result):
        if not node:
            return 
        
        self.recursion(node.left, result)
        self.recursion(node.right, result)
        result.append(node.val)
    
    def iteration(self, node, result):
        if not node:
            return
        
        stack = []
        while node or stack:
            if node:
                stack.append(node)
                result.append(node.val)
                node = node.right
            else:
                node = stack.pop()
                node = node.left
        
        result.reverse()
    
    def morris(self, node, reuslt):
        if not node:
            return
        
        while node:
            if not node.right:
                result.append(node.val)
                node = node.left
            else:
                predecessor = node.right
                while predecessor.left and predecessor.left != node:
                    predecessor = predecessor.left
                
                if not predecessor.left:
                    predecessor.left = node
                    result.append(node.val)
                    node = node.right
                else:
                    predecessor.left = None
                    node = node.left
        
        result.reverse()