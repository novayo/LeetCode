class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @functools.lru_cache(None)
        def p1MaxScore(idx, is_p1):
            if idx >= len(stoneValue):
                return 0
            
            if is_p1:
                ret = -float('inf')
                for i in range(1, 4):
                    ret = max(ret, sum(stoneValue[idx: idx+i]) + p1MaxScore(idx + i, False))
                return ret
            else:
                ret = float('inf')
                for i in range(1, 4):
                    ret = min(ret, p1MaxScore(idx + i, True))
                return ret
        
        p1 = p1MaxScore(0, True)
        p2 = sum(stoneValue) - p1
        
        if p1 > p2:
            return 'Alice'
        elif p1 == p2:
            return 'Tie'
        else:
            return 'Bob'
