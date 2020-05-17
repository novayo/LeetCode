class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        dp = collections.defaultdict(list)
        dp[1] = []
        dp2 = {}
        ans = []
        for i in range(2, n+1):
            
            # run self
            l = 1
            r = i
            tmp = l/r
            while tmp < 1:
                tmp = l/r
                if tmp >= 1:
                    break
                if tmp not in dp2:
                    dp2[tmp] = str(l) + "/" + str(r)
                dp[i].append(dp2[tmp])
                l += 1
            
            ans += dp[i]
            
        return list(set(ans))
