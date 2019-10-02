class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if nums1 == nums2 == []:
            return 0.0
        
        index_median = (len(nums1)+len(nums2))//2 + 1
        i, j = 0, 0
        pre = ans = 0.0
        while i+j < index_median:
            if i < len(nums1) and j == len(nums2):
                i += 1
                if i+j == index_median:
                    ans = nums1[i-1]
                    break
                pre = nums1[i-1]
            elif i == len(nums1) and j < len(nums2):
                j += 1
                if i+j == index_median:
                    ans = nums2[j-1]
                    break
                pre = nums2[j-1]
            elif nums1[i] < nums2[j]:
                i += 1
                if i+j == index_median:
                    ans = nums1[i-1]
                    break
                pre = nums1[i-1]
            else:
                j += 1
                if i+j == index_median:
                    ans = nums2[j-1]
                    break
                pre = nums2[j-1]
        
        if (len(nums1)+len(nums2))%2 == 0:
            return (pre+ans)/2
        else:
            return ans
            
