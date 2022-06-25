class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def recr(a, b, k):
            if not a:
                return b[k]
            elif not b:
                return a[k]
            
            ia, ib = len(a) // 2, len(b) // 2
            
            if ia + ib < k:
                if a[ia] > b[ib]:
                    return recr(a, b[ib+1:], k - (ib + 1))
                else:
                    return recr(a[ia+1:], b, k - (ia + 1))
            else:
                if a[ia] > b[ib]:
                    return recr(a[:ia], b, k)
                else:
                    return recr(a, b[:ib], k)
        
        m = len(nums1)
        n = len(nums2)
        
        if (m+n) % 2 == 0:
            return (recr(nums1, nums2, (m+n)//2) + recr(nums1, nums2, (m+n)//2-1)) / 2
        else:
            return recr(nums1, nums2, (m+n)//2)
        
