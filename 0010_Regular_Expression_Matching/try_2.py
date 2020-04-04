class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        
        def dp(sindex, pindex):
            if (sindex, pindex) not in memo:
                if pindex == len(p):
                    ans = sindex == len(s)
                else:
                    isValid = sindex < len(s) and p[pindex] in {s[sindex], '.'}
                    if pindex+1 < len(p) and p[pindex+1] == '*':
                        ans = dp(sindex, pindex+2) or (isValid and dp(sindex+1, pindex))
                    else:
                        ans = isValid and dp(sindex+1, pindex+1)
                memo[sindex, pindex] = ans
            return memo[sindex, pindex]
        
        return dp(0,0)
