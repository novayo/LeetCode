# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        '''
        return 從i~j能組合出來的樹(list)
        此node去分別接上左邊跟右邊
        '''
        if n == 0:
            return []
        
        def recr(start, end):
            if start > end:
                return [None]
            
            ret = []
            
            for i in range(start, end+1):
                left = recr(start, i-1)
                right = recr(i+1, end)
                
                
                if left != None:
                    for l in left:
                        for r in right:
                            node = TreeNode(i)
                            node.left = l
                            node.right = r
                            ret.append(node)
                else:
                    for r in right:
                        for l in left:
                            node = TreeNode(i)
                            ret.left = l
                            node.right = r
                            ret.append(node)
            
            return ret
        
        return recr(1, n)