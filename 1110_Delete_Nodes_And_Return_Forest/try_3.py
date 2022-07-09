# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        '''
        O(n) time / O(w + d) space
        - n is the number of nodes of the input tree and w is the width and d is the depth.
        '''
        def isMarked(node):
            return node.val in to_delete
        
        def dfs(node, que):
            if not node:
                return node
            
            if isMarked(node):
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                return None
            else:
                node.left = dfs(node.left, que)
                node.right = dfs(node.right, que)
                return node
        
        to_delete = set(to_delete)
        ans = []
        
        que = collections.deque([root])
        while que:
            node = que.popleft()
            if not isMarked(node):
                ans.append(node)
            
            dfs(node, que)
        
        return ans
