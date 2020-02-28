class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bit = 0
        for n in nums:
            bit ^= n
        return bit
