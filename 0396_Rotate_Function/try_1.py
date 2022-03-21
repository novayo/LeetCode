class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
        '''
        f(i+1) = sum(A) + A[-1] * (-length) + f(i)
        '''
        
        sumA = sum(nums)
        n = len(nums)
        f_0 = ans = sum([nums[i] * i for i in range(n)])
        
        for i in range(n-1, 0, -1):
            f_i = sumA + nums[i] * -n + f_0
            ans = max(ans, f_i)
            f_0 = f_i
        
        return ans