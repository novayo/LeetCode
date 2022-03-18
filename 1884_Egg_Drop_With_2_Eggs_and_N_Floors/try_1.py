class Solution:
    def twoEggDrop(self, n: int) -> int:
        memo = {}
        def recr(start, end):
            if start > end:
                return 0
            
            if (start, end) not in memo:
                memo[start, end] = float('inf')
                for i in range(start, end+1):
                    memo[start, end] = min(
                        memo[start, end],
                        1 + max(i-start, recr(i+1, end))
                    )
            return memo[start, end]
        
        return recr(1,n)