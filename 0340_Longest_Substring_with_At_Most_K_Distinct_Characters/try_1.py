class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hash_table = collections.defaultdict(int)
        
        i = tmp_k = ans = 0
        for j in range(len(s)):
            if hash_table[s[j]] == 0:
                tmp_k += 1
            hash_table[s[j]] += 1
            
            if tmp_k > k:
                while tmp_k > k:
                    hash_table[s[i]] -= 1
                    if hash_table[s[i]] == 0:
                        tmp_k -= 1
                    i += 1
            ans = max(ans, j-i+1)
                
        return ans
