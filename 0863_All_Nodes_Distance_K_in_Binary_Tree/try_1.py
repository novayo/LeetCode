# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def dfs(node):
            if not node:
                return
            
            if node.left:
                node.left.parent = node
                dfs(node.left)
                
            if node.right:
                node.right.parent = node
                dfs(node.right)
        
        dfs(root)
        root.parent = None
        
        ans = []
        visited = set([target.val])
        queue = [(target, 0)]
        while queue:
            node, _k = queue.pop()
            
            if _k == k:
                ans.append(node.val)
                continue
            
            if node.left and node.left.val not in visited:
                queue.append((node.left, _k+1))
                visited.add(node.left.val)
                
            if node.right and node.right.val not in visited:
                queue.append((node.right, _k+1))
                visited.add(node.right.val)
                
            if node.parent and node.parent.val not in visited:
                queue.append((node.parent, _k+1))
                visited.add(node.parent.val)
        
        return ans