# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        '''
        因為是BST
            從小到大 => 慢慢找下一個successor   => inorder traversal
            從大到小 => 慢慢找上一個predecessor
        '''
        stack1 = []
        stack2 = []
        while True:

            while root1:
                stack1.append(root1)
                root1 = root1.left
            
            while root2:
                stack2.append(root2)
                root2 = root2.right
            
            if len(stack1) == 0 or len(stack2) == 0:
                break
            
            _sum = stack1[-1].val + stack2[-1].val
            if _sum == target:
                return True
            elif _sum < target:
                root1 = stack1.pop().right
            else:
                root2 = stack2.pop().left
        
        return False
