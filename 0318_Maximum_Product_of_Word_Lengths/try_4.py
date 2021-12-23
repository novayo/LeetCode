class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dp = collections.defaultdict(int)
        
        for word in words:
            mask = 0
            for w in word:
                index = ord(w)-ord('a')
                mask |= 2**index
            dp[mask] = max(dp[mask], len(word))
        
        ans = 0
        for key1, value1 in dp.items():
            for key2, value2 in dp.items():
                if key1 & key2 > 0:
                    continue
                ans = max(ans, value1*value2)
        
        return ans