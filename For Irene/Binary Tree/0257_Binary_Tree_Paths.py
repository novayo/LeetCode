# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        '''
        node
            loop node.left, node.right bottom-up result
        
            return type: list
        '''
        
        def dfs(node):
            if not node:
                return []
            
            left_list = dfs(node.left)
            right_list = dfs(node.right)
            
            ret = []
            
            if not left_list and not right_list:
                return [str(node.val)]
            
            for l_result in left_list:
                ret.append(str(node.val) + '->' + l_result)

            for r_result in right_list:
                ret.append(str(node.val) + '->' + r_result)
                
            return ret
        
        return dfs(root)
        
        