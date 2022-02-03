# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        l, r = 0, 10**4-1
        
        while l <= r:
            mid = l + (r-l) // 2
            val = reader.get(mid)
            if val > target:
                r = mid-1
            elif val == target:
                return mid
            else:
                l = mid + 1
        return -1
        
