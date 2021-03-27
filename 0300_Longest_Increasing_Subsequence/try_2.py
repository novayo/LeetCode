class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        
        for num in nums:
            index = bisect.bisect_left(tails, num)
            if index >= len(tails):
                tails.append(num)
            else:
                tails[index] = num
        
        return len(tails)
