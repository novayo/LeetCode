class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        dp = collections.defaultdict(int)
        bitmask = 0
        
        dp[bitmask] = 1
        for w in word:
            bitmask ^= 1 << (ord(w) - ord('a'))
            ans += dp[bitmask]
            for i in range(10):
                ans += dp[bitmask ^ (1<<i)]
            dp[bitmask] += 1
        return ans