class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n^2)
        '''
        暴力解的話，需要一直去往下看下一個的最大是多少，
        因此可以用dp去存起來（存大於幾個人，自己算一個），並之後去查找就可以了，
        只是這樣會有個bug，
        就是 會不知道要抓後面誰的dp，
        假設 5,10,11,6,7,8，那以5來說，在dp的時候，要抓10（dp=2）的還是抓6（dp=3）呢？
        所以還是得去跑過後面的所有dp，
        並且，
        讓 >5的值的dp去做max就可以找到ans了，
        就是要去測試 5,10  ;  5,11  ;  5,6  ;  5,7  ;  5,8 看哪個最大（因為dp是記自己大於幾人）。
        '''
        ans = 0
        dp = [0] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            tmp = 0
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    tmp = max(tmp, dp[j])
            dp[i] = tmp + 1
            ans = max(ans, dp[i])
        
        return ans
