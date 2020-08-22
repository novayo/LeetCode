# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # binary search
        '''
        直接把範圍設計在0~10^4，直接用binary search去找即可
        '''
        left, right = 0, 10**4
        while left < right:
            mid = left + (right - left) // 2
            ret = reader.get(mid)
            if ret > target:
                right = mid
            elif ret == target:
                return mid
            else:
                left = mid + 1
        return -1
