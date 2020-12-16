class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        '''
        N = (x+1) + ... + (x+k)
        N = xk + (1+k)k//2
        N - (1+k)k//2 = xk
        => (N - (1+k)k//2) % k == 0 就是其中一個答案
        '''
        
        ans = 0
        upper = (-1+sqrt(1+8*N))//2+1

        for i in range(1, int(upper)):
            if (N - (1+i)*i//2) % i == 0:
                ans += 1
                
        return ans