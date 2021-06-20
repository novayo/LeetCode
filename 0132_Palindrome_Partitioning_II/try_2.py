class Solution:
    def minCut(self, s: str) -> int:

        def isPalindrome_odd(startIndex: int, dp: dict):
            l, r = startIndex, startIndex # for odd
            dp[l].append(r)
            
            while l-1 >= 0 and r+1 < len(s):
                if s[l-1] == s[r+1]:
                    l -= 1
                    r += 1
                    dp[l].append(r)
                else:
                    break
            
            return l, r
        
        def isPalindrome_even(startIndex: int, dp: dict):
            l, r = startIndex, startIndex+1 # for even
            dp[l].append(r)
            
            while l-1 >= 0 and r+1 < len(s):
                if s[l-1] == s[r+1]:
                    l -= 1
                    r += 1
                    dp[l].append(r)
                else:
                    break
            
            return l, r
        
        dp = collections.defaultdict(list)
        for i in range(len(s)):
            l, r = isPalindrome_odd(i, dp)
            
            if i+1 < len(s) and s[i] == s[i+1]:
                l, r = isPalindrome_even(i, dp)
        
        
        def recr(startIndex, memo={}):
            
            if startIndex >= len(s):
                return 0
        
            if startIndex in memo:
                return memo[startIndex]
        
            ans = float('inf')
            for next_pos in dp[startIndex][::-1]:
                ans = min(ans, recr(next_pos+1) + 1)
                
            memo[startIndex] = ans
            return memo[startIndex]
        
        ans = recr(0, {})
        return ans - 1