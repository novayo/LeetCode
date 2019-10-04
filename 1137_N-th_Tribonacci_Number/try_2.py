class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        elif n<3: return 1
        pre1, pre2, pre3, ans = 0, 1, 1, 0
        for i in range(n-2):
            ans = pre1 + pre2 + pre3
            pre1 = pre2
            pre2 = pre3
            pre3 = ans
        
        return ans
