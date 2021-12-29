# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        arr1 = []
        arr2 = []
        
        def inorder(node, arr):
            if not node:
                return
            
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)
        
        inorder(root1, arr1)
        inorder(root2, arr2)
        
        
        ret = []
        i = j = 0
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                ret.append(arr1[i])
                i += 1
            else:
                ret.append(arr2[j])
                j += 1
        
        while i < len(arr1):
            ret.append(arr1[i])
            i += 1
        
        while j < len(arr2):
            ret.append(arr2[j])
            j += 1
        
        return ret