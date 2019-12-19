# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        stack1 = collections.deque()
        stack2 = collections.deque()

        while True:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            
            while root2:
                stack2.append(root2)
                root2 = root2.right

            if not stack1 or not stack2: break
            
            tmp1 = stack1[-1]
            tmp2 = stack2[-1]
                
            if tmp1.val + tmp2.val == target:
                return True
            elif tmp1.val + tmp2.val < target:
                root1 = stack1.pop().right
            else:
                root2 = stack2.pop().left

        return False
