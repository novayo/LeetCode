class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [False] * len(s)
        stack = []
        
        for i in range(len(s)):
            if s[i] == ')':
                if stack:
                    dp[stack.pop()] = dp[i] = True
            else:
                stack.append(i)
        
        ans = 0
        tmp = 0
        for v in dp:
            if v:
                tmp += 1
                ans = max(ans, tmp)
            else:
                tmp = 0
        return ans
