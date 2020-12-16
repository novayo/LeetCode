class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        '''
        sliding window
        '''

        def calculate_top(lower, target):
            if lower > target:
                return lower + 1
            return ceil(-1+sqrt(1+4*lower*lower-4*lower+8*target)/2)
        
        i = 1
        ans = 0
        j = calculate_top(1, N)
        
        sum = (1+j)*j//2
                
        while i + j <= N:
            # print(sum, j)
            if sum < N:
                j += 1
                sum += j
            elif sum == N:
                ans += 1
                j += 1
                sum += j 
            else:
                new_i = calculate_top(i, sum-N)
                sum -= (i+new_i)*(new_i-i+1) // 2
                i = new_i + 1
        
        return ans+1