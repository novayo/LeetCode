class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        next = pre = 0
        for i in range(1, n+1):
            next = (pre << int(log2(i))+1) + i
            next %= MOD
            pre = next
        return pre