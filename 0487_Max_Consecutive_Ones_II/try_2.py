class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        遇到第一個1就繼續往下，直到遇到第二個1就往前數到第二個1之後再繼續跑
        '''
        
        left = 0
        ans = 0
        zeros = 0
        k = 1 # 可以翻幾張0，這裡為1
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans
