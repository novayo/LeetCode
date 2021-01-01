class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        A以選擇拿或不拿，A拿了B不拿，A不拿B拿
        所以就變成了背包問題
        但要轉成A是否能拿到total的一半
        '''
        
        total = sum(nums)
        
        # 如果不能整除代表不能分割為兩段
        if total % 2 != 0:
            return False
        
        
        dp = {}
        def knapsack(backpack, index):
            
            if (backpack, index) in dp:
                return dp[backpack, index]
            
            if backpack == 0:
                return True
            
            if index < 0 or backpack < 0:
                dp[backpack, index] = False
                return dp[backpack, index]
            
            if knapsack(backpack, index-1) or knapsack(backpack-nums[index], index-1):
                dp[backpack, index] = True
                return dp[backpack, index]
            else:
                dp[backpack, index] = False
                return dp[backpack, index]
            
        
        return knapsack(total//2, len(nums)-1)
