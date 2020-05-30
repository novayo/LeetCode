class Solution:
    def countBits(self, num: int) -> List[int]:
        '''
        0 0   0
        1 1  1
        
        2 10  1
        3 11  2
        
        4 100
        5 101
        6 110
        7 111
        
        8
        9
        '''
        if num == 0:
            return [0]
        if num == 1:
            return [0, 1]
        dp = [0, 1]
        i = 0
        n = 2
        
        while n<=num:
            if log(n, 2).is_integer():
                i = 0
            dp.append(dp[i]+1)
            n += 1
            i += 1
        return dp
