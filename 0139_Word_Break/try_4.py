class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        
        for i in range(n+1):
            for word in wordDict:
                if i < len(word):
                    continue
                
                if dp[i-len(word)] and s[i-len(word): i] == word:
                    dp[i] = True
        
        return dp[n]

