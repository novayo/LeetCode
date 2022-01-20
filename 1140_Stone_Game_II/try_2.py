class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        memo = {}
        
        def recr(flag, index, M):
            
            if (flag, index, M) in memo:
                return memo[flag, index, M]
            
            if index >= len(piles):
                return 0
            
            if flag:
                ret = -float('inf')
                for m in range(1, 2*M+1):
                    ret = max(ret, sum(piles[index:index+m]) + recr(not flag, index+m, max(m, M)))
            else:
                ret = float('inf')
                for m in range(1, 2*M+1):
                    ret = min(ret, recr(not flag, index+m, max(m, M)))
            
            memo[flag, index, M] = ret
            return memo[flag, index, M]
        
        return recr(True, 0, 1)
                              
