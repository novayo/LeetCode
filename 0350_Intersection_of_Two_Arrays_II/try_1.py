class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums2_counter = collections.Counter(nums2)
        
        for num1 in nums1:
            tmp = nums2_counter.get(num1, 0)
            if tmp > 0:
                ans.append(num1)
                nums2_counter[num1] -= 1
        return ans
