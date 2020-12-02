# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        把p與q的path記起來為兩的list，之後去比較最後一個相同的
        '''
        
        def findPath(node, path, pPath, qPath):
            if pPath != [] and qPath != []:
                return
            
            if not node:
                return
            
            if node == p:
                pPath.append(path[:] + [node])
            
            if node == q:
                qPath.append(path[:] + [node])
            
            findPath(node.left, path + [node], pPath, qPath)
            findPath(node.right, path + [node], pPath, qPath)
        pPath = []
        qPath = []
        findPath(root, [], pPath, qPath)
        
        if (len(pPath[0]) > len(qPath[0])):
            pPath, qPath = qPath, pPath
            
        i = 0
        while i < len(pPath[0]) and pPath[0][i] == qPath[0][i]:
            i += 1
        return pPath[0][i-1]