class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        
        def recr(flag, left, right):
            nonlocal memo
            if left > right:
                return 0
            if (flag, left, right) in memo:
                return memo[flag, left, right]
            
            if flag:
                ret = -float('inf')
                ret = max(piles[left] + recr(not flag, left+1, right),
                          piles[right]+ recr(not flag, left, right-1))
            else:
                ret = float('inf')
                ret = min(recr(not flag, left+1, right),
                          recr(not flag, left, right-1))
            
            memo[flag, left, right] = ret
            return ret
        
        return sum(piles) < recr(True, 0, len(piles)-1) * 2
