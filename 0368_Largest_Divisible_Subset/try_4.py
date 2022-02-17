class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        '''
        LIS: 往前找第一個能整除的+1即可
        '''
        nums.sort()
        n = len(nums)
        dp = [1] * n
        track = {} # track => 把關係式紀錄起來 => track[16] = 8, track[8] = 4, track[4] = 2
        
        for i, num in enumerate(nums):
            for j in range(i-1, -1, -1):
                if (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0) and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
                    track[i] = j
        
        # 找第一個最大值的位置出來
        index = 0
        for i in range(n):
            if dp[index] < dp[i]:
                index = i
        
        # 將答案串起來
        ans = [nums[index]]
        while index in track:
            index = track[index]
            ans.append(nums[index])
        return ans