class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        dp[i] => 0~i 是合格的
        
        跑兩個for => 找所有組合
        目前有在wordDict內，(i~j)則確保 dp[i-1] = True => dp[j] = True
        
        return dp[len(s)-1]
        '''
        wordDict = set(wordDict)
        dp = [False] * (len(s)+1)
        
        dp[0] = True
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict and dp[i] == True:
                    dp[j] = True
        
        return dp[-1]