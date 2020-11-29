# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        以preorder為基準，從左邊往右邊
        應當先建立左邊再建立右邊，要符合preorder的建立順序
        '''
        
        position = {}
        for i in range(len(inorder)):
            position[inorder[i]] = i
        
        def recr(left, right):
            if left > right:
                return
            
            root = TreeNode(preorder.pop(0))
            index = position[root.val]
            
            root.left = recr(left, index-1)
            root.right = recr(index+1, right)            
            return root
        
        return recr(0, len(inorder)-1)
