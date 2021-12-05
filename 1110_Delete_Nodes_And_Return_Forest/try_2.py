# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        '''
        dfs => 等左邊 右邊做完之後，若有要刪除，再把左右加入list，並讓這格為None
        
        若root沒有在to_delete => 則最後要加進list
        '''
        
        def dfs(node, ans):
            if not node:
                return
            
            node.left = dfs(node.left, ans)
            node.right = dfs(node.right, ans)
            
            if node.val in to_delete_set:
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
                return None
            
            return node
        
        ans = []
        to_delete_set = set(to_delete)
        r = dfs(root, ans)
        if r != None:
            ans.append(r)
        return ans
        
