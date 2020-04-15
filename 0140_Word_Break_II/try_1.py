class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        wordDict = set(wordDict)
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        if not dp[-1]:
            return []
        
        
        # print(dp)
        ans = []
        def dfs(start, List):
            if start >= len(s):
                ans.append(' '.join(List))
                return
            
            if dp[start]:
                for i in range(start, len(s)+1):
                    if dp[i] and s[start:i] in wordDict:
                        dfs(i, List + [s[start:i]])
        dfs(0,[])
        return ans
