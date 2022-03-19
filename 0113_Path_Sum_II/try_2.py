# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        def recr(node, cur_sum, cur_list):
            nonlocal ans 
            if not node.left and not node.right:
                if cur_sum + node.val == targetSum:
                    cur_list.append(node.val)
                    ans.append(tuple(cur_list[:]))
                    cur_list.pop()
                return
            
            if node.left:
                recr(node.left, cur_sum + node.val, cur_list + [node.val])
            if node.right:
                recr(node.right, cur_sum + node.val, cur_list + [node.val])
        
        recr(root, 0, [])
        return ans