class Solution:
    def numWays(self, n: int, k: int) -> int:
        '''
        2 * 1 * 1
        2 * 1 * 2
        
        3 * 1 * 2
        3 * 2 * 3
        
        
        a = 目前不一樣
        b = 目前一樣
        
        a => 下次不一樣 => a*(k-1)
        a => 下次一樣 => a*1
        b => 下次不一要 => b*(k-1)
        '''
        
        a, b = k, 0
        
        for i in range(n-1):
            next_a = a*(k-1) + b*(k-1)
            next_b = a
            
            a, b = next_a, next_b
        
        return a+b
