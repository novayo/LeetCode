class Solution:
    def longestPrefix(self, s: str) -> str:
        ans = ""
        
        n = len(s)
        for res in range(n-1, 0, -1) : 
            prefix = s[0: res] 
            suffix = s[n - res: n] 

            if (prefix == suffix) : 
                ans = prefix
                break

        return ans
