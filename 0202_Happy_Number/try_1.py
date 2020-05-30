class Solution:
    def isHappy(self, n: int) -> bool:
        dp = set()
        while n != 1:
            _tuple = ()
            _sum = 0
            while n>0:
                mod = n%10
                _tuple += (mod,)
                _sum += (mod)**2
                n //= 10
            if _tuple in dp:
                return False
            else:
                dp.add(_tuple)
                n = _sum
        return True
