class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        x1, (x2 x3), x4, x5
        y1, y2, y3, (y4  y5), y6
        
        => x2 < x3, y5 => 做bs => if x2 > y5 => false
        => y4 < x3, y5
        
        
        => mid1 + mid2 = (m+n+1) // 2
        => mid2 = (m+n+1) // 2 - mid1
        
        -> odd => ans = max(x2, y4)
        -> even => ans = (max(x2, y4) + min(x3, y5)) // 5
        '''
        m = len(nums1)
        n = len(nums2)
        
        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1
        
        if m == 0:
            if n % 2 == 0:
                return (nums2[n//2] + nums2[n//2-1]) / 2
            else:
                return nums2[n//2]
        
        l, r = 0, m
        while l <= r:
            i = l + (r-l) // 2
            j = (m + n + 1)//2 - i
            
            if i > 0 and j < n and nums1[i-1] > nums2[j]:
                r = i - 1
            elif j > 0 and i < m and nums1[i] < nums2[j-1]:
                l = i + 1
            else:
                x1 = -float('inf') if i == 0 else nums1[i-1]
                x2 = float('inf') if i == m else nums1[i]
                y1 = -float('inf') if j == 0 else nums2[j-1]
                y2 = float('inf') if j == n else nums2[j]
                
                if (m+n) % 2 == 0:
                    return (max(x1, y1) + min(x2, y2)) / 2
                else:
                    return max(x1, y1)
        return -1
                    