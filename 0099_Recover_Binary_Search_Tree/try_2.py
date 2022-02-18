# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        perform inorder and swap two error node's val
        '''
        
        def visit():
            if pre_visited and pre_visited.val > node.val:
                if not first_node:
                    first_node = pre_visited
                    second_node = node
                else:
                    second_node = node

            pre_visited = node
        
        pre_visited = first_node = second_node = None
        node = root
        
        while node:
            if not node.left:
                # visit
                if pre_visited and pre_visited.val > node.val:
                    if not first_node:
                        first_node = pre_visited
                        second_node = node
                    else:
                        second_node = node
                pre_visited = node
                node = node.right
            else:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                
                if predecessor.right != node:
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    # visit
                    if pre_visited and pre_visited.val > node.val:
                        if not first_node:
                            first_node = pre_visited
                            second_node = node
                        else:
                            second_node = node
                    pre_visited = node
                    node = node.right
        
        first_node.val, second_node.val = second_node.val, first_node.val