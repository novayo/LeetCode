class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        找最小長度的 combination
        然後查看 num2的各種 長度是否有在 combination 內
        
        => binary search
        '''
        def condition(length):
            # find combination of nums1
            comb = set()
            i, j = 0, length
            while j <= len(nums1):
                comb.add(tuple(nums1[i:j]))
                i, j = i+1, j+1
            
            # find nums2
            i, j = 0, length
            while j <= len(nums2):
                if tuple(nums2[i:j]) in comb:
                    return True
                i, j = i+1, j+1
            return False
        
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        min_length = min(len(nums1), len(nums2))
        l, r = 1, min_length
        ans = 0
        while l <= r:
            mid = l + (r-l) // 2
            if condition(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans
            
        
        
        
