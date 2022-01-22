class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = 0
        for num in nums:
            ans ^= num
        
        # find any 1 in bin(ans)
        bin_1_in_ans = 2**(len(bin(ans)[2:])-1)
        
        other_ans = 0
        for num in nums:
            if bin_1_in_ans & num == 0:
                other_ans ^= num
        
        return other_ans, ans ^ other_ans
