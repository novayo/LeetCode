class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set
        return list(set(nums1)&set(nums2))
