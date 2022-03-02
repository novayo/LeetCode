class Node:
    def __init__(self, val, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r
        self.left_node = None
        self.right_node = None

class segment_tree:
    def __init__(self, arr):
        self.root = self.build(0, len(arr)-1, arr)
    
    def build(self, l, r, arr):
        if l == r:
            return Node(arr[l], l, r)
        
        mid = l + (r-l) // 2
        root = Node(arr[mid], l, r)
        root.left_node = self.build(l, mid, arr)
        root.right_node = self.build(mid+1, r, arr)
        root.val = min(root.left_node.val, root.right_node.val)
        return root
    
    def query(self, l, r):
        def _query(node, l, r):
            if l == node.l and r == node.r:
                return node.val
            
            mid = node.l + (node.r-node.l) // 2
            if r <= mid:
                return _query(node.left_node, l, r)
            elif l > mid:
                return _query(node.right_node, l, r)
            else:
                return min(_query(node.left_node, l, mid), _query(node.right_node, mid+1, r))
        return _query(self.root, l, r)
                
        
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        tree = segment_tree(arr)
        ans = 0
        
        n = len(arr)
        for length in range(1, n+1):
            for i in range(n-length+1):
                ans += tree.query(i, i+length-1)
        return ans