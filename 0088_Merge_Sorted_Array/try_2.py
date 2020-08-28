class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        從尾巴看回來（指標k）
        
        如果nums1[i] < nums2[j]，則nums1[k] = nums2[j]，j -= 1，k -= 1
        如果nums1[i] >= nums2[j]，則nums1[k] = nums1[i]，i -= 1，k -= 1
        
        但
        [4,0,0,0,0,0]
        [1,2,3,5,6]
        這種情況i會先結束，而j會指向3，而出現[4,0,0,4,5,6]
        所以還得將123補上
        nums1[:j+1] = nums2[:j+1]
        '''
        i = m-1
        j = n-1
        k = m+n-1
        
        while i>=0 and j>=0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        nums1[:j+1] = nums2[:j+1]
