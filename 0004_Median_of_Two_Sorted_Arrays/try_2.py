class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tmp, i, j = [], 0, 0
        
        for k in range((len(nums1)+len(nums2))//2 + 1):
            if i >= len(nums1) and j < len(nums2):
                tmp.append(nums2[j])
                j += 1
            elif j >= len(nums2) and i < len(nums1):
                tmp.append(nums1[i])
                i += 1
            else:
                if nums1[i] < nums2[j]:
                    tmp.append(nums1[i])
                    i += 1
                else:
                    tmp.append(nums2[j])
                    j += 1
        if (len(nums1) + len(nums2)) % 2 is 0:
            return (tmp[-1] + tmp[-2])/2
        else:
            return tmp[-1]
