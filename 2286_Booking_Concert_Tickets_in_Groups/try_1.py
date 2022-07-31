class Node:
    def __init__(self, val, left_index, right_index, left=None, right=None):
        self.val = val
        self.left_index = left_index
        self.right_index = right_index
        self.left = left
        self.right = right

class SegmentTree:
    def __init__(self, n, m):
        self.root = self.build(0, n-1, m)
    
    def build(self, i, j, m):
        if i > j:
            return None
        if i == j:
            return Node(m, i, j)
        
        mid = i + (j-i) // 2
        left = self.build(i, mid, m)
        right = self.build(mid+1, j, m)
        return Node(max(left.val, right.val), i, j, left, right)
    
    def update(self, i, val):
        def _update(node, i, val):
            if node.left_index == node.right_index == i:
                node.val = val
                return
            
            mid = node.left_index + (node.right_index - node.left_index) // 2
            if i <= mid:
                _update(node.left, i, val)
            else:
                _update(node.right, i, val)
            
            if node.left and node.right:
                node.val = max(node.left.val, node.right.val)
            elif node.left:
                node.val = node.left.val
            elif node.right:
                node.val = node.right.val
        
        _update(self.root, i, val)
    
    def query(self, i, j):
        def _query(node, i, j):
            if i > j:
                return 0

            if node.left_index == i and node.right_index == j:
                return node.val
            
            mid = node.left_index + (node.right_index - node.left_index) // 2
            if j <= mid:
                return _query(node.left, i, j)
            elif i > mid:
                return _query(node.right, i, j)
            else:
                return max(_query(node.left, i, mid), _query(node.right, mid+1, j))
        return _query(self.root, i, j)

class BIT:
    def __init__(self, n, m):
        self.presum = [0] * (n+1)
        for i in range(n):
            self.update(i, m)
    
    def update(self, i, diff):
        i += 1
        while i < len(self.presum):
            self.presum[i] += diff
            i += i & -i
    
    def query(self, i):
        ret = 0
        i += 1
        while i > 0:
            ret += self.presum[i]
            i -= i & -i
        return ret

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.start = 0
        self.arr = [m] * (n+1)
        self.segtree = SegmentTree(n, m)
        self.bit = BIT(n, m)

    def gather(self, k: int, maxRow: int) -> List[int]:
        ans = -1
        l, r = 0, maxRow
        
        while l <= r:
            mid = l + (r-l) // 2
            if self.segtree.query(l, mid) >= k:
                ans = mid
                r = mid - 1
            elif self.segtree.query(mid, r) >= k:
                ans = mid
                l = mid + 1
            else:
                break
                
        if ans == -1:
            return []
        
        pre = self.arr[ans]
        self.segtree.update(ans, pre-k)
        self.bit.update(ans, -k)
        self.arr[ans] = pre-k
        return [ans, self.m - pre]

    def scatter(self, k: int, maxRow: int) -> bool:
        if self.bit.query(maxRow) < k:
            return False
        
        start = self.start
        for i in range(start, maxRow+1):
            pre = self.arr[i]
            
            if pre >= k:
                self.segtree.update(i, pre-k)
                self.bit.update(i, -k)
                self.arr[i] = pre-k
                break
            else:
                k -= pre
                self.segtree.update(i, 0)
                self.bit.update(i, -pre)
                self.arr[i] = 0
                self.start = max(self.start, i)
        
        return True


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)