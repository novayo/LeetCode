# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node, container):
            if not node:
                return
            
            inorder(node.left, container)
            container.append(node.val)
            inorder(node.right, container)
        
        list1, list2 = [], []
        inorder(root1, list1)
        inorder(root2, list2)
        
        
        ans = []
        i1, i2 = 0, 0
        
        while i1 < len(list1) and i2 < len(list2):
            if list1[i1] <= list2[i2]:
                ans.append(list1[i1])
                i1 += 1
            else:
                ans.append(list2[i2])
                i2 += 1
        
        if i1 < len(list1):
            ans.extend(list1[i1:])
            
        
        if i2 < len(list2):
            ans.extend(list2[i2:])
        
        return ans