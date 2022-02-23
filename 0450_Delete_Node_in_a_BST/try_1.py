# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def recr(val):
            nonlocal root
            
            # find target node
            pre_node = None
            node = root
            while node and node.val != val:
                pre_node = node
                if node.val > val:
                    node = node.left
                else:
                    node = node.right
            
            # if node not in tree
            if not node:
                return
            
            # case 1: no children
            if not node.left and not node.right:
                if node == root:
                    root = None
                else:
                    if pre_node.val > val:
                        pre_node.left = None
                    else:
                        pre_node.right = None
            
            # case 2: one children
            elif not node.left:
                if node == root:
                    root = node.right
                else:
                    if pre_node.val > val:
                        pre_node.left = node.right
                    else:
                        pre_node.right = node.right
                        
            elif not node.right:
                if node == root:
                    root = node.left
                else:
                    if pre_node.val > val:
                        pre_node.left = node.left
                    else:
                        pre_node.right = node.left
            
            # case 3: two children
            else:
                predecessor = node.left
                while predecessor.right:
                    predecessor = predecessor.right
                
                tmp = predecessor.val
                recr(predecessor.val)
                node.val = tmp
                
        recr(key)  
        return root
                        