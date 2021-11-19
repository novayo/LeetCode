class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
        + -法 => 最後最小的數字，但要比0大
        '''
        _sum = sum(stones)
        dp = {}
        dp[1] = collections.defaultdict(int)
        dp[1][stones[0]] += 1
        dp[1][-stones[0]] += 1
        
        ans = stones[0]
        for i in range(2, len(stones)+1):
            dp[i] = collections.defaultdict(int)
            for j in range(-_sum, _sum+1):
                dp[i][j] = dp[i-1][j-stones[i-1]] + dp[i-1][j+stones[i-1]]
                
                if i == len(stones) and j >= 0 and dp[i][j] > 0:
                    return j
        
        for j in range(0, _sum+1):
            if dp[len(stones)][j] > 0:
                return j
        
