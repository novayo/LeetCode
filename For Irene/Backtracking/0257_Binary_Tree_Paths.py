# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans = []
        
        def backtracking(node, cur_list):
            nonlocal ans
            
            if not node.left and not node.right:
                cur_list.append(str(node.val))
                ans.append('->'.join(cur_list)) # include leaf
                cur_list.pop()
                return
            
            if node.left:
                cur_list.append(str(node.val))
                backtracking(node.left, cur_list)
                cur_list.pop()
            
            if node.right:
                cur_list.append(str(node.val))
                backtracking(node.right, cur_list)
                cur_list.pop()
        
        backtracking(root, [])
        return ans