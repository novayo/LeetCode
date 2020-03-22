class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = bin(n)[-1:1:-1]
        reverse += (32-len(reverse)) * '0'
        return int(reverse, 2)

