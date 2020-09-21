class Solution:
    def fib(self, N: int) -> int:
        '''
        relation: f(i) = f(i-1) + f(i-2)
        base case: 0:1, 1:1
        '''
        
        table = {0: 0, 1:1}
        
        def recr(n):
            
            if n in table:
                return table[n]
            else:
                table[n] = recr(n-1) + recr(n-2)
            
            return table[n]
        
        return recr(N)