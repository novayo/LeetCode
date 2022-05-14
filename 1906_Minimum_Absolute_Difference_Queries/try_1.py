class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        
        dp = [[0] * 101]
        for i in range(n):
            dp.append(dp[-1][:])
            dp[-1][nums[i]] += 1
        
        
        ans = []
        for i, j in queries:
            avaliable = []
            for idx, (a, b) in enumerate(zip(dp[i], dp[j+1])):
                if a != b:
                    avaliable.append(idx)
            
            if len(avaliable) < 2:
                ans.append(-1)
            else:
                tmp = float('inf')
                for idx in range(1, len(avaliable)):
                    tmp = min(tmp, avaliable[idx] - avaliable[idx-1])
                ans.append(tmp)
        
        return ans
