class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tmp = collections.Counter(nums)
        return max(tmp, key=tmp.get)
