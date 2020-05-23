class Solution:
    def countAndSay(self, n: int) -> str:
        dp = {1:"1#"}
        
        for i in range(2, n+1):
            next_str = ""
            
            same = None
            for s in dp[i-1]:
                if not same:
                    same = [s, 1]
                else:
                    if s == same[0]:
                        same[1] += 1
                    else:
                        next_str += (str(same[1])+same[0])
                        same = [s, 1]
            dp[i] = next_str + '#'
            
        return dp[n][:-1]
