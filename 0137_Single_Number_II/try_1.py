class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = two = 0
        for num in nums:
            one = (one ^ num) & (~two)
            two = (two ^ num) & (~one)
        
        return one
            
