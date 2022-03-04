class Solution:
    def countArrangement(self, n: int) -> int:
        '''
        任兩個能否整除，若所有的都能配對，則回傳True
        '''
        memo = {}
        def recr(index, bitmask):
            if index > n:
                return 1
            
            if (index, bitmask) not in memo:
                ret = 0
                for _n in range(1, n+1):
                    if bitmask & 2**_n != 0:
                        continue
                    if _n % index == 0 or index % _n == 0:
                        ret += recr(index+1, bitmask | 2**_n)
                memo[index, bitmask] = ret
            return memo[index, bitmask]
        return recr(1, 0)
        
