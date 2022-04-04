# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # monotonic stack
        if not nums:
            return []
        
        min_stack = []
        for num in nums:
            node = TreeNode(num)
            last_pop = None
            
            while min_stack and min_stack[-1].val < num:
                last_pop = min_stack.pop()
            node.left = last_pop
            
            if min_stack:
                min_stack[-1].right = node
            min_stack.append(node)
        
        return min_stack[0]
