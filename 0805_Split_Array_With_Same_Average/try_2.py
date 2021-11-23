class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        '''
        sum / n = sumA / k = sumB / (n-k)
        sum / n * k = sumA
        
        1. dp[i][k][n] = 前i個，取k個，能否組成n = False => 這個代表sumA
        
        2. 
        因為knapsack的定義是sum(nums)，當總和很大，不管長度小或大，都會TLE
        那就乾脆找出取前k個的組合
        dp[i] = 取前k個排列組合的set => 代表sumA
        dp[0] = set[0]
        
        之後再去check答案即可
        '''
        sum_num = sum(nums)
        n = len(nums)
        
        dp = [set() for i in range(n+1)]
        dp[0] = set([0])
        
        # 那就乾脆找出取前k個的組合
        for num in nums:
            for k in range(n-1, 0, -1):
                if len(dp[k-1]) > 0:
                    for v in dp[k-1]:
                        dp[k].add(v+num)
        
        # check答案
        for k in range(1, n+1):
            if sum_num * k / n in dp[k]:
                return True
        return False
