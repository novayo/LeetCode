class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        '''
        left <- index -> right
        if all left < index <= all right:
            return True
        '''
        n = len(nums)
        left_max = [-float('inf')] * n
        right_min = [float('inf')] * n
        
        cur_max = -float('inf')
        for i in range(n):
            num = nums[i]
            left_max[i] = cur_max
            if num > cur_max:
                cur_max = num
        
        cur_min = float('inf')
        for i in range(n-1, -1, -1):
            num = nums[i]
            right_min[i] = cur_min
            if num < cur_min:
                cur_min = num
        
        ans = 0
        for i, num in enumerate(nums):
            left, right = left_max[i], right_min[i]
            if left < num <= right:
                ans += 1
        return ans
