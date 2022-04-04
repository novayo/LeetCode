class Node:
    def __init__(self, val, l_index, r_index, left=None, right=None):
        self.val = val
        self.l_index = l_index
        self.r_index = r_index
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self, arr):
        self.root = self.build(arr)
    
    def build(self, arr):
        def _build(l, r):
            if l == r:
                return Node(arr[l], l, r)
            
            mid = l + (r-l) // 2
            left = _build(l, mid)
            right = _build(mid+1, r)
            return Node(max(left.val, right.val), l, r, left, right)
        
        return _build(0, len(arr)-1)
    
    def query(self, l, r):
        def _query(root, l, r):
            if l > r:
                return -float('inf')
            if root.l_index == l and root.r_index == r:
                return root.val
            
            mid = root.l_index + (root.r_index-root.l_index) // 2
            if mid > r:
                return _query(root.left, l, r)
            elif mid < l:
                return _query(root.right, l, r)
            else:
                return max(
                    _query(root.left, l, mid),
                    _query(root.right, mid+1, r)
                )
        
        return _query(self.root, l, r)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        index = {}
        for i, num in enumerate(nums):
            index[num] = i
        
        tree = SegmentTree(nums)
        def build(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])
            
            _max_num = tree.query(l, r)
            mid = index[_max_num]
            
            left = build(l, mid-1)
            right = build(mid+1, r)
            return TreeNode(_max_num, left, right)
        
        return build(0, len(nums)-1)
