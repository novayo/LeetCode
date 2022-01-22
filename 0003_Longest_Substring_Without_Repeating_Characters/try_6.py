class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        hash + sliding window
        '''
        
        index = {}
        ans = i = j = 0
        
        while j < len(s):
            _s = s[j]
            if _s in index:
                i = max(i, index[_s] + 1)
            index[_s] = j
            ans = max(ans, j-i+1)
            j += 1
            
        return ans
