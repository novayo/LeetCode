class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def condition(length):
            set_nums1 = set()
            for i in range(len(nums1) - length + 1):
                set_nums1.add(tuple(nums1[i:i+length]))
            
            for i in range(len(nums2) - length + 1):
                if tuple(nums2[i:i+length]) in set_nums1:
                    return True
            return False
        
        l, r = 0, min(len(nums1), len(nums2)) + 1
        while l < r:
            mid = (r-l) // 2 + l
            if condition(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1

