class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        swap, not_swap = 1, 0
        
        for i in range(n-2, -1, -1):
            _swap = _not_swap = float('inf')
            
            if nums1[i] < nums2[i+1] and nums2[i] < nums1[i+1]:
                _not_swap = min(_not_swap, swap)
                _swap = min(_swap, not_swap)
            
            if nums1[i] < nums1[i+1] and nums2[i] < nums2[i+1]:
                _swap = min(_swap, swap)
                _not_swap = min(_not_swap, not_swap)
             
            swap, not_swap = _swap+1, _not_swap
            
        return min(swap, not_swap)
