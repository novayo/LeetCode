class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def maxP1Score(player1, i, j):
            if i > j:
                return 0
            
            if (i, j) in memo:
                return memo[i, j]
            
            if player1:
                memo[i, j] = max(maxP1Score(False, i+1, j) + piles[i], maxP1Score(False, i, j-1) + piles[j])
            else:
                memo[i, j] = min(maxP1Score(True, i+1, j), maxP1Score(True, i, j-1))
            return memo[i, j]
        
        p1 = maxP1Score(True, 0, len(piles)-1)
        p2 = sum(piles) - p1
        return p1 > p2
