class Solution:
    def getMoneyAmount(self, n: int) -> int:
        
        memo = {}
        def recr(l, r):
            
            if l >= r:
                return 0
            if (l, r) in memo:
                return memo[l, r]
            
            ret = float('inf')
            for pick in range((l+r)//2, r+1):
                left = recr(l, pick-1)
                right = recr(pick+1, r)
                
                ret = min(ret, max(left, right) + pick)
            
            memo[l, r] = ret
            return memo[l, r]
        
        return recr(1, n)