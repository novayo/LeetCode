class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        '''
        stone game 1概念，只是得分變成以下兩點
        選左邊：sum[j]-sum[i+1]，選取範圍變為i+1~j
        選右邊：sum[j-1]-sum[i]，選取範圍變為i~j-1
        
        recr回傳：當前選擇的人可以選擇的最大值
        '''
        length = len(stones)
        sumOfStones = [0]
        for stone in stones:
            sumOfStones.append(stone + sumOfStones[-1])
        
        # base
        dp = [[0 for _ in range(length)] for _ in range(length)]
            
        # bottom-up
        for j in range(1, length):
            for i in range(j-1, -1, -1):
                dp[i][j] = max(
                    sumOfStones[j+1]-sumOfStones[i+1] - dp[i+1][j],
                    sumOfStones[j]-sumOfStones[i] - dp[i][j-1]
                )
        return dp[0][-1]
