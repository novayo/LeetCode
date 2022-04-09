class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        dp = []
        
        # init
        for c in range(65, 91):
            dp.append([0] * 26 + [-c])
        
        # loop
        for string in votes:
            for i, _s in enumerate(string):
                dp[ord(_s)-ord('A')][i] += 1
        
        # sort
        dp.sort(reverse=True)
        
        # ans
        ans = ""
        for x in dp:
            ans += chr(-x[-1])
        
        return ans[:len(votes[0])]
        