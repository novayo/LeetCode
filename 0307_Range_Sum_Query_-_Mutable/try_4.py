class Node:
    def __init__(self, val, start, end, left=None, right=None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class segmental_tree:
    def __init__(self, nums):
        self.root = self.build(nums, 0, len(nums)-1)
    
    def build(self, nums, start, end):
        if start == end:
            return Node(nums[start], start, end)
        
        mid = (start + end) // 2
        left = self.build(nums, start, mid)
        right = self.build(nums, mid+1, end)
        
        value = 0
        if left:
            value += left.val
        if right:
            value += right.val
        
        return Node(value, start, end, left, right)
    
    def update(self, index, value):
        self._update(self.root, index, index, value)
    
    def query(self, left, right):
        return self._query(self.root, left, right)
    
    def _update(self, root, start, end, value):
        if start > end:
            return
        
        if root.start == start and root.end == end:
            root.val = value
            return
        
        mid = (root.start + root.end) // 2
        if end <= mid:
            self._update(root.left, start, end, value)
        elif mid < start:
            self._update(root.right, start, end, value)
        else:
            self._update(root.left, start, mid, value)
            self._update(root.right, mid+1, end, value)
            
        root.val = 0
        if root.left:
            root.val += root.left.val
        if root.right:
            root.val += root.right.val
    
    def _query(self, root, start, end):
        if start > end:
            return 0
        
        if root.start == start and root.end == end:
            return root.val
        
        mid = (root.start + root.end) // 2
        if end <= mid:
            return self._query(root.left, start, end)
        elif mid < start:
            return self._query(root.right, start, end)
        else:
            return self._query(root.left, start, mid) + self._query(root.right, mid+1, end)

class NumArray:

    def __init__(self, nums: List[int]):
        self.segTree = segmental_tree(nums)

    def update(self, index: int, val: int) -> None:
        self.segTree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segTree.query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)