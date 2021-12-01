class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        dp = collections.defaultdict(int)
        
        for start, end in intervals:
            dp[start] += 1
            dp[end] -= 1
            
        ans = cur = 0
        for time in sorted(dp.keys()):
            cur += dp[time]
            ans = max(ans, cur)
        
        return ans
            
