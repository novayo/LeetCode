# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        head = TreeNode(preorder[0])
        stack = [head]
        
        for i in range(1, len(preorder)):
            if stack[-1].val > preorder[i]:
                stack[-1].left = TreeNode(preorder[i])
                stack.append(stack[-1].left)
            else:
                tmp = None
                while stack and stack[-1].val < preorder[i]:
                    tmp = stack.pop()
                tmp.right = TreeNode(preorder[i])
                stack.append(tmp.right)
        return head
