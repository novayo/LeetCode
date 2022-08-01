class Solution:
    def checkRecord(self, n: int) -> int:
        '''
        < 2 A
        < 3 L in a row
        
        0A0L 
            A -> 1A0L
            P -> 0A0L
            L -> 0A1L
        0A1L
            A -> 1A0L
            P -> 0A0L
            L -> 0A2L
        0A2L
            A -> 1A0L
            P -> 0A0L
            L -> x
        1A0L
            A -> x
            P -> 1A0L
            L -> 1A1L
        1A1L
            A -> x
            P -> 1A0L
            L -> 1A2L
        1A2L
            A -> x
            P -> 1A0L
            L -> x
        '''
        MOD = 10**9 + 7
        _0A0L, _0A1L, _0A2L, _1A0L, _1A1L, _1A2L = 1, 0, 0, 0, 0, 0
        
        for i in range(n):
            t_0A0L, t_0A1L, t_0A2L, t_1A0L, t_1A1L, t_1A2L = _0A0L, _0A1L, _0A2L, _1A0L, _1A1L, _1A2L
            
            _0A0L = (t_0A0L + t_0A1L + t_0A2L) % MOD
            _0A1L = (t_0A0L) % MOD
            _0A2L = (t_0A1L) % MOD
            _1A0L = (t_0A0L + t_0A1L + t_0A2L + t_1A0L + t_1A1L + t_1A2L) % MOD
            _1A1L = (t_1A0L) % MOD
            _1A2L = (t_1A1L) % MOD
        
        return sum([_0A0L, _0A1L, _0A2L, _1A0L, _1A1L, _1A2L]) % MOD
        
