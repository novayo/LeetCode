class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        counter = collections.Counter()
        ans = i = 0

        for j in range(n):
            counter[s[j]] += 1
            while len(counter) > k:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    del counter[s[i]]
                i += 1
            
            ans = max(ans, j-i+1)
        
        return ans