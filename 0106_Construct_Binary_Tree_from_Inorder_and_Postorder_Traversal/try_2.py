# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        '''
        以postorder為基準
        為了減少index查詢時間，用hash把他存起來，那recr也要改成用左右邊的方式去標示現在的inorder要存取到哪裡
        '''
        position = {}
        for i in range(len(inorder)):
            position[inorder[i]] = i
        
        def recr(left, right):
            if left > right:
                return

            rootVal = postorder.pop()
            index = position[rootVal]
            root = TreeNode(rootVal)

            root.right = recr(index+1, right)
            root.left = recr(left, index-1)
            return root
        
        return recr(0, len(inorder)-1)
