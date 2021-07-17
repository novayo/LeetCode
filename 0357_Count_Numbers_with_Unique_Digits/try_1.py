class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        ans, f_k = 0, 1
        for i in range(n):
            if i == 0:
                ans += 10
                f_k = 9
            else:
                f_k *= (10-i)
                ans += f_k
        return ans