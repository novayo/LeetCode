class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        '''
        the same as stone game 2: find(A-B) maximum
        '''
        
        dp = collections.defaultdict(int)
        
        # return Alice - Bob
        def recr(index):
            if index >= len(stoneValue):
                dp[index] = 0
                return dp[index]
            
            if index in dp:
                return dp[index]
            
            tmp = -float('inf')
            for i in range(1, 4):
                tmp = max(tmp, sum(stoneValue[index:index+i]) - recr(index+i))
            dp[index] = tmp
            return dp[index]
        
        ans = recr(0)
        if ans > 0:
            return "Alice"
        elif ans == 0:
            return "Tie"
        else:
            return "Bob"
