class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        
        # True
        dp[-1] = True
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if s[i:j] in wordDict and dp[j] is True:
                    dp[i] = True
        
        return dp[0]
        
