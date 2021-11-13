class SegmentTreeNode:
    def __init__(self, val, start, end, left=None, right=None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self, n):
        self.root = self.build(0, n-1)
    
    def build(self, start, end, val=0):
        if start == end:
            return SegmentTreeNode(val, start, end)
        
        mid = (start + end) // 2
        left = self.build(start, mid, val)
        right = self.build(mid+1, end, val)
        return SegmentTreeNode(val, start, end, left, right)
    
    def query(self, start, end):
        return self._query(start, end, self.root)
    
    def _query(self, start, end, node):
        if node.start == start and node.end == end:
            return node.val
        
        mid = (node.start + node.end) // 2
        if end <= mid:
            return self._query(start, end, node.left)
        elif mid < start:
            return self._query(start, end, node.right)
        else:
            return self._query(start, mid, node.left) + \
                   self._query(mid+1, end, node.right)
    
    def update(self, index):
        self._update(index, 1, self.root)
    
    def _update(self, index, val, node):
        if node.start == node.end == index:
            node.val += val
            return
        
        mid = (node.start + node.end) // 2
        
        if index <= mid:
            self._update(index, val, node.left)
        else:
            self._update(index, val, node.right)
            
        node.val = node.left.val + node.right.val

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        tmp = sorted(list(set(nums)))
        index = {}
        for i in range(len(tmp)):
            index[tmp[i]] = i
        
        tree = SegmentTree(len(tmp))
        ans = []
        for num in nums[::-1]:
            i = index[num]
            if i == 0:
                ans.append(0)
            else:
                ans.append(tree.query(0, i-1))
            tree.update(i)
            
        return ans[::-1]
