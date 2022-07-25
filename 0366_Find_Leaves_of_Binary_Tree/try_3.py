'''
len(root) > 0
return list of value


O(n) time / O(n+d) space
    1
  2   3         -> d = 2
4  5            -> d = 1

1.left
 => [[4,5], [2]]

1.right
 => [[3]]

merge left, right
[[4,5, 3], [2], [1]]
'''

# Input: root = [1,2,3,4,5]
# Output: [[4,5,3],[2],[1]]
# Explanation:
# [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        # O(n) time / O(n+d) space - where n is the number of the input tree and d is the depth.
        def dfs(node):
            if not node:
                return []
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            merged_list = []
            for i in range(max(len(left), len(right))):
                merged_list.append([])
                
                if i < len(left):
                    merged_list[-1] += left[i]
                if i < len(right):
                    merged_list[-1] += right[i]
                    
            return merged_list + [[node.val]]
        
        return dfs(root)
