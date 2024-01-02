class Node:
    def __init__(self, val, start, end, left=None, right=None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self, array):
        self.root = self.build(0, len(array)-1, array)
    
    def build(self, start, end, array):
        if start > end:
            return None
        if start == end:
            return Node(array[start], start, end)
        
        mid = end + (start - end) // 2
        left = self.build(start, mid, array)
        right = self.build(mid + 1, end, array)

        _sum = (left.val if left else 0) + (right.val if right else 0)
        return Node(_sum, start, end, left, right)
    
    def query(self, start, end):
        def _query(root, start, end):
            if start > end:
                return 0
            if start == root.start and end == root.end:
                return root.val
            
            mid = root.end + (root.start - root.end) // 2
            if end < mid:
                return _query(root.left, start, end)
            elif mid < start:
                return _query(root.right, start, end)
            else:
                return _query(root.left, start, mid) + _query(root.right, mid+1, end)
        return _query(self.root, start, end)
    
    def update(self, idx, val):
        def _update(root, start, end, val):
            if start > end:
                return
            if start == root.start and end == root.end:
                root.val = val
                return
            
            mid = root.end + (root.start - root.end) // 2
            if end < mid:
                _update(root.left, start, end, val)
            elif mid < start:
                _update(root.right, start, end, val)
            else:
                _update(root.left, start, mid, val)
                _update(root.right, mid+1, end, val)
            
            root.val = (root.left.val if root.left else 0) + (root.right.val if root.right else 0)
        _update(self.root, idx, idx, val)

class NumArray:

    def __init__(self, nums: List[int]):
        self.segment_tree = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segment_tree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.segment_tree.query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
