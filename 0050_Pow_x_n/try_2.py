class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        n = 13
        則 先找出 1: x, 2:x^2, 4:x^4, 8:x^8，之後停止，因為下一個就大於n了
        之後就
        n  - count = n
        13 - 8     = 5
        5  - 4     = 1
        （因為1<2，所以跳過2）
        1  - 1     = 0
        
        之後就相乘 ans = 1 * table[8] * table[4] * table[1]
        '''
        
        if n < 0:
            x = 1/x
            n = -n
        
        count = 1
        table = {0:1, 1:x}
        while count * 2 <= n:
            table[count*2] = table[count]*table[count]
            count *= 2

        ans = 1
        while n > 0:
            if n - count >= 0:
                ans *= table[count]
                n -= count
            count //= 2
        return ans
