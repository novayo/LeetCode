# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        if n % 2 == 0:
            return []
        
        memo = {}
        
        def recr(rest):
            if rest <= 0:
                return [None]
            if rest == 1:
                return [TreeNode()]
            
            if rest in memo:
                return memo[rest]
            
            ret = set()
            for i in range(1, rest-1, 2):
                left = recr(i)
                right = recr(rest-1-i)
                
                for l_node in left:
                    for r_node in right:
                        node = TreeNode()
                        node.left = l_node
                        node.right = r_node
                        ret.add(node)
            
            memo[rest] = ret
            return memo[rest]
        
        return recr(n)
