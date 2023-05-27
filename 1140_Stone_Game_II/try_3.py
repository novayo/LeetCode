class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @functools.lru_cache(None)
        def maxP1Score(player, idx, M):
            if idx == len(piles):
                return 0
            
            if player:
                _ret = curSum = 0
                for m in range(1, 2*M+1):
                    if idx + m > len(piles):
                        break
                    curSum += piles[idx+m-1]
                    _ret = max(_ret, maxP1Score(False, idx+m, max(M, m)) + curSum)
                return _ret
            else:
                _ret = float('inf')
                for m in range(1, 2*M+1):
                    if idx + m > len(piles):
                        break
                    _ret = min(_ret, maxP1Score(True, idx+m, max(M, m)))
                return _ret
            
        return maxP1Score(True, 0, 1)
