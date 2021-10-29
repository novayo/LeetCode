class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # 排序好後，每個index 找 之前list中最大的數值 % == 0 => 代表跟此list其餘的也可以整除
        dp = {}
        
        for num in sorted(nums):
            tmp = []
            for key in dp:
                if num % key == 0:
                    if len(dp[key]) > len(tmp):
                        tmp = dp[key].copy()
            tmp.append(num)
            dp[num] = tmp
        
        return sorted(dp.values(), key=len, reverse=True)[0]
                    
