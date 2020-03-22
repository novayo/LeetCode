class SegmentTreeNode:
    def __init__(self, _start: int, _end: int, _min: int, _index: int, _left, _right):
        self.start = _start
        self.end = _end
        self.min = _min
        self.index = _index
        self.left = _left
        self.right = _right

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if heights == []:
            return 0
        
        # build min segment tree
        root = self.buildSegmentTree(0, len(heights)-1, heights)
        
        def dfs(i, j):
            if i > j:
                return 0
            
            _, minIndex = self.querySegmentTree(root, i, j)
            return max(heights[minIndex]*(j-i+1), max(dfs(i, minIndex-1), dfs(minIndex+1, j)))
        
        return dfs(0, len(heights)-1)
    
    def buildSegmentTree(self, start: int, end: int, target: List):
        if start == end:
            return SegmentTreeNode(start, end, target[start], start, None, None)
        mid = (start+end) // 2
        left = self.buildSegmentTree(start, mid, target)
        right = self.buildSegmentTree(mid+1, end, target)
        
        returnMin = None
        returnIndex = 0
        if left.min <= right.min:
            returnMin = left.min
            returnIndex = left.index
        else:
            returnMin = right.min
            returnIndex = right.index
        return SegmentTreeNode(start, end, returnMin, returnIndex, left, right)
    
    def querySegmentTree(self, root: SegmentTreeNode, i: int, j: int):
        if root.start == i and root.end == j:
            return root.min, root.index
        mid = (root.start+root.end)//2
        
        # target range locates on left node
        if j <= mid:
            return self.querySegmentTree(root.left, i, j)
        elif mid < i:
            return self.querySegmentTree(root.right, i, j)
        else:
            return min(self.querySegmentTree(root.left, i, mid), self.querySegmentTree(root.right, mid+1, j))
