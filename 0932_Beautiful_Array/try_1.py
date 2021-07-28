class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        ''' 左邊放2n-1 右邊放2n
        '''
        memo = {1: [1]}
        
        def recr(n):
            if n not in memo:
                left = recr((n+1) // 2)
                right = recr(n // 2)
                memo[n] = [2*x-1 for x in left] + [2*x for x in right]
            return memo[n]
        
        return recr(n)
