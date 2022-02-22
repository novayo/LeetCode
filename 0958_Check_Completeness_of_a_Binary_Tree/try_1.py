# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        '''
        number nodes and check each layer
            must be sequential number in each layer
        '''
        
        stack = [(root, 1)]
        layer = 0
        
        while stack:
            next_layer = []
            
            start, end = 2**layer, 2**(layer+1)
            
            for node, number in stack:
                if start == number:
                    start += 1
                    if node.left:
                        next_layer.append((node.left, number*2))
                    if node.right:
                        next_layer.append((node.right, number*2+1))
                else:
                    return False
            
            if start != end and len(next_layer) > 0:
                print(start, end)
                return False
            
            stack = next_layer
            layer += 1
        
        return True