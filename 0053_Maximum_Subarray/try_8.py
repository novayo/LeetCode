class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def recr(i, j):
            if i > j:
                return -float('inf')
            
            mid = i + (j - i) // 2
            
            # find left
            left_max = -float('inf')
            cur_sum = 0
            for k in range(mid-1, i-1, -1):
                cur_sum += nums[k]
                left_max = max(left_max, cur_sum)
            
            # find right
            right_max = -float('inf')
            cur_sum = 0
            for k in range(mid+1, j+1):
                cur_sum += nums[k]
                right_max = max(right_max, cur_sum)
            
            return max(
                nums[mid],
                nums[mid] + left_max,
                nums[mid] + right_max,
                nums[mid] + left_max + right_max,
                recr(i, mid-1),
                recr(mid+1, j)
            )
        
        return recr(0, len(nums)-1)
        