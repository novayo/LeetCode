class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        def match(_dict):
            count = 0
            for k, v in _dict.items():
                if v % 2 == 1:
                    count += 1
                    if count > 1:
                        return False
            return True
        
        ans = 0
        n = len(word)
        dp = [collections.defaultdict(int) for _ in range(n)]
        
        for length in range(1, n+1):
            idx = 0
            for i in range(length-1, n):
                dp[idx][word[i]] += 1
                    
                if match(dp[idx]):
                    ans += 1
                    
                idx += 1
        return ans