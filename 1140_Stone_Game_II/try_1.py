class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        dp = collections.defaultdict(int)
        def recr(index, M):
            
            if index + 2*M >= len(piles):
                dp[index, M] = sum(piles[index:])
                return dp[index, M]
            
            if (index, M) in dp:
                return dp[index, M]
            
            tmp = -float('inf')
            for i in range(1, 2*M + 1):
                tmp = max(tmp, sum(piles[index: index+i])-recr(index+i, max(i, M)))
            dp[index, M] = tmp
            return dp[index, M]
        
        return (sum(piles)+recr(0,1))//2
