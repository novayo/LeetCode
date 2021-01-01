class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        '''
        stone game 1概念，只是得分變成以下兩點
        選左邊：sum[j]-sum[i+1]，選取範圍變為i+1~j
        選右邊：sum[j-1]-sum[i]，選取範圍變為i~j-1
        
        recr回傳：當前選擇的人可以選擇的最大值
        '''
        
        sumOfStones = [0]
        for stone in stones:
            sumOfStones.append(stone + sumOfStones[-1])
        
        dp = {}
        def recr(i, j):
            
            if i == j:
                dp[i, j] = 0
                return dp[i, j]
            
            dp[i, j] = max(
                sumOfStones[j+1]-sumOfStones[i+1] - recr(i+1, j),
                sumOfStones[j]-sumOfStones[i] - recr(i, j-1)
            )
            
            return dp[i, j]
        
        return recr(0, len(stones)-1)
