# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        go_right = True
        ans = []
        
        queue = collections.deque([root])
        while queue:
            next_queue = collections.deque()
            layer_val = []
            
            while queue:
                if go_right:
                    node = queue.popleft()
                    if node.left:
                        next_queue.append(node.left)
                    if node.right:
                        next_queue.append(node.right)
                else:
                    node = queue.pop()
                    if node.right:
                        next_queue.appendleft(node.right)
                    if node.left:
                        next_queue.appendleft(node.left)
                
                layer_val.append(node.val)
            
            queue = next_queue
            ans.append(layer_val)
            go_right = not go_right
        
        return ans