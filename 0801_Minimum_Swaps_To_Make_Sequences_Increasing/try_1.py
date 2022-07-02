class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        def isValid(i):
            return i < 1 or (nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i])
        
        @functools.lru_cache(None)
        def recr(i, isSwap):
            if i >= n:
                return 0

            ret1 = ret2 = float('inf')
            
            if isValid(i):
                ret1 = recr(i+1, False)
                
            nums1[i], nums2[i] = nums2[i], nums1[i]
            if isValid(i):
                ret2 = 1 + recr(i+1, True)
            nums1[i], nums2[i] = nums2[i], nums1[i]
            return min(ret1, ret2)
        
        return recr(0, False)
