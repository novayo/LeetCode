class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Sliding Window
        dp = {}
        for i in range(len(s)):
            dp[i] = abs(ord(t[i]) - ord(s[i]))
         
        ans, left, right = 0, 0, 0
        while right < len(s):
            maxCost -= dp[right]
            if maxCost < 0:
                maxCost += (dp[right] + dp[left])
                left += 1
            else:
                right += 1
            ans = max(ans, right-left)
            
        return ans
