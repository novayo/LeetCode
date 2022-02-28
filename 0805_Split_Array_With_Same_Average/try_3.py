class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        '''
        average => t / t_length = sumA / lengthA == sumB / lengthB
        sumA = t * lengthA / t_length
            => 若發現此運算式可能為整數 => 則check是否有機會在長度為lengthA的情況下，組成sumA
        '''
        memo = {}
        def recr(index, sumA, lengthA):
            if lengthA == 0:
                return sumA == 0
            
            if index >= n or sumA < 0:
                return False
            
            if (index, sumA, lengthA) in memo:
                return memo[index, sumA, lengthA]
            
            memo[index, sumA, lengthA] = recr(index+1, sumA-nums[index], lengthA-1) or recr(index+1, sumA, lengthA)
            return memo[index, sumA, lengthA]
        
        
        t = sum(nums)
        n = len(nums)
        for lengthA in range(1, n):
            if (t * lengthA) % n == 0:
                if recr(0, t * lengthA // n, lengthA):
                    return True
        return False
