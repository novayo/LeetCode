class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        A以選擇拿或不拿，A拿了B不拿，A不拿B拿
        所以就變成了背包問題
        但要轉成A是否能拿到total的一半
        '''
        length = len(nums)
        total = sum(nums)
        
        # 如果不能整除代表不能分割為兩段
        if total % 2 != 0:
            return False
        
        # base
        dp = [[0] for _ in range(length)]
        
        # bottom-up
        for i in range(1, length):
            seen = set()
            for pre in dp[i-1]:
                tmp = nums[i] + pre
                
                if tmp == total // 2:
                    return True
                
                # 不拿
                if pre not in seen:
                    seen.add(pre)
                    dp[i].append(pre)
                
                # 拿
                if tmp not in seen:
                    seen.add(tmp)
                    dp[i].append(tmp)
        return False
