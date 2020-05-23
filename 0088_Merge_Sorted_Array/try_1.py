class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m-1
        j1 = m+n-1
        i2 = n-1
        
        while i1>=0 and i2>=0:
            if nums2[i2] >= nums1[i1]:
                nums2[i2], nums1[j1] = nums1[j1], nums2[i2]
                i2 -= 1
                j1 -= 1
            else:
                nums1[i1], nums1[j1] = nums1[j1], nums1[i1]
                i1 -= 1
                j1 -= 1
        
        if i1 == -1:
            while j1 >= 0:
                nums1[j1], nums2[i2] = nums2[i2], nums1[j1]
                j1 -= 1
                i2 -= 1

