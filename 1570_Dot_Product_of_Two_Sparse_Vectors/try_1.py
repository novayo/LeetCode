class SparseVector:
    def __init__(self, nums: List[int]):
        self.v1 = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.v1[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        a, b = self.v1, vec.v1
        if len(a) > len(b):
            a, b = b, a
        
        ans = 0
        for key, value in a.items():
            if key in b:
                ans += b[key] * value
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
