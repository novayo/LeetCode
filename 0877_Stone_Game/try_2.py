class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        '''
        Recursion: 找尋i~j中，能拿得max是多少
        若A選左邊則(剩下部分為B拿的max)，因此piles[i] - dp[i+1][j]
        若A選右邊則(剩下部分為B拿的max)，因此piles[j] - dp[i][j-1]
        這兩個值要取max
        '''
        
        length = len(piles)
        dp = [[0] * length for i in range(length)]
        
        # Base Case
        for i in range(length):
            dp[i][i] = piles[i]
        
        # bottom-up
        for j in range(1, length):
            for i in range(j-1, -1, -1):
                dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
        
        return dp[0][-1]> 0
