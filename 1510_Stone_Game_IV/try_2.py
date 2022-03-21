class Solution:
    def winnerSquareGame(self, n: int) -> bool:
           
        Alice_win = [False] * (n+1)
        Alice_win[1] = True
        
        for i in range(2, n+1):
            for attempt in range(int(sqrt(i)), 0, -1):
                if Alice_win[i-attempt**2] == False:
                    Alice_win[i] = True
                    break
        return Alice_win[n]