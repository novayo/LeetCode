class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        '''
        int to string and find length
        '''
        
        ans = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                ans += 1
        return ans
