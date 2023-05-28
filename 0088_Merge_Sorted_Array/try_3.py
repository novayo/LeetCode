class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1, i2, k = m-1, n-1, m+n-1
        
        while i1 >= 0 and i2 >= 0:
            if nums1[i1] <= nums2[i2]:
                nums1[k] = nums2[i2]
                k, i2 = k-1, i2-1
            else:
                nums1[k] = nums1[i1]
                k, i1 = k-1, i1-1
        
        while i2 >= 0:
            nums1[k] = nums2[i2]
            k, i2 = k-1, i2-1
