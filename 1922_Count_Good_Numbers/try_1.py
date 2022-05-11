class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = pow(10, 9) + 7
        odd = pow(4, n//2, MOD)
        even = pow(5, ceil(n/2), MOD)
        return (odd * even) % MOD