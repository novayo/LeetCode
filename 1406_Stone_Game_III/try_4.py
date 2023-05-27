class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @functools.lru_cache(None)
        def maxP1Score(player, idx):
            if idx == len(stoneValue):
                return 0
            
            if player:
                ret = -float('inf')
                curSum = 0
                for i in range(1, 3+1):
                    if idx + i > len(stoneValue):
                        break
                    curSum += stoneValue[idx+i-1]
                    ret = max(ret, curSum + maxP1Score(False, idx + i))
                return ret
            else:
                ret = float('inf')
                for i in range(1, 3+1):
                    if idx + i > len(stoneValue):
                        break
                    ret = min(ret, maxP1Score(True, idx + i))
                return ret
        
        p1 = maxP1Score(True, 0)
        p2 = sum(stoneValue) - p1
        if p1 > p2:
            return "Alice"
        elif p1 == p2:
            return "Tie"
        else:
            return "Bob"
