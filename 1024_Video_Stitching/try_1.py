class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        '''
        dp = [0~time]
        
         0 1 2 3 4 5 6 7 8 9 10
        [1,1,1,2,2,2,2,2,2,2, 3]
        '''
        dp = [float('inf')] * (time+1)
        
        # loop
        for start, end in sorted(clips):
            for i in range(start, min(end, time)+1):
                if start == 0:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i], dp[start]+1)
        
        return -1 if dp[time] == float('inf') else dp[time]