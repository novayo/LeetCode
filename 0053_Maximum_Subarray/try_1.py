class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide(left, right):
            if left>right: return -float('inf')
            middle = (left+right)//2
            l = divide(left, middle-1)
            r = divide(middle+1, right)
            l_m_r = conquer(left, middle, right)
            return max(max(l, r), l_m_r)
        
        def conquer(left, middle, right):
            _sum = sumLeft = 0
            for i in range(middle-1, left-1, -1):
                _sum += nums[i]
                sumLeft = max(sumLeft, _sum)
            
            _sum = sumRight = 0
            for i in range(middle+1, right+1):
                _sum += nums[i]
                sumRight = max(sumRight, _sum)
            return sumLeft + nums[middle] + sumRight
        
        return divide(0, len(nums)-1)
