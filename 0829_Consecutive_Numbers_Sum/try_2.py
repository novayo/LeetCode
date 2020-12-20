class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        '''
        N = (x+1) + ... + (x+k)
        N = xk + (1+k)k//2
        N - (1+k)k//2 = xk
        => (N - (1+k)k//2) % k == 0 就是其中一個答案
        =>N * 2 = k(2x + k + 1), k(2x + k + 1)一定是 一奇*一偶
        '''
        
        ans = 0
        
        '''
        那一奇*一偶的話，那2要全部丟給偶數，所以多餘的2不會影響結果，因此可以把2都除掉，只需要專注在有幾個奇數即可
        '''
        while N%2 == 0:
            N //= 2
            
        '''
        因為2*N會變成長方形，而長*寬會是長方形的總和，所以去loop的時候，i一定要是2*N的因數
        而找到的i是代表 (i=2 * 5)=10，一組的
        因此找到最小因數即可，而最小因數即為sqrt(2*N)
        '''
        upper = sqrt(2*N)+1

        for i in range(1, int(upper)):
            if (N - (1+i)*i//2) % i == 0:
                ans += 1
                
        return ans