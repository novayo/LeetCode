# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # inorder + binary search
        '''
        因為是bst，先用inorder把整個tree轉成list (sorted)，
        之後再用binary search找到值即可
        
        time complexity: O(n + logn)
        space complexity: O(n)
        '''
        
        # 用inorder把整個tree轉成list (sorted)
        tree = []
        
        def inorder(node):
            nonlocal tree
            if not node:
                return
            inorder(node.left)
            tree.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        
        # binary search
        left, right = 0, len(tree)-1
        while left < right:
            mid = left + (right - left) // 2
            if tree[mid] > target:
                right = mid
            else:
                left = mid + 1
        
        if abs(target - tree[left-1]) < abs(target - tree[left]):
            return tree[left-1]
        else:
            return tree[left]
