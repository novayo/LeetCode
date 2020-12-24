class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        '''
        dp[i] = 為true or false => 輪到誰，誰就是true or false
        因為另一個人會聰明的選擇
        
        所以 就變成去找說，因為都是Alex先選擇，所以就看目前的dp[n去減平方數]有沒有等於False，代表Alex選擇了此平方數之後，Bob絕對會輸，有的話這格就為True，否則為False
        同時可以建立平方數的表
        '''
        
        def isSqrt(num):
            tmp = int(sqrt(num))
            return tmp == sqrt(num)
        
        square = []
        dp = [False] * (n+1)
        
        for i in range(1, n+1):
            if isSqrt(i):
                square.append(i)
            
            for s in square[::-1]:
                if dp[i-s] == False:
                    dp[i] = True
                    break
        return dp[-1]
