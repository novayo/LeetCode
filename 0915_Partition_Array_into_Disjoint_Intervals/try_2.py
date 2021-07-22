class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left = collections.deque()
        right = collections.deque()
        
        left_max, right_min = -float('inf'), float('inf')
        left.append(left_max)
        right.appendleft(right_min)
        for i in range(len(nums)):
            if nums[i] > left_max:
                left_max = nums[i]
            
            if nums[~i] < right_min:
                right_min = nums[~i]
            
            left.append(left_max)
            right.appendleft(right_min)
        
        for i in range(len(nums)):
            _left = left[i+1]
            _right = right[i+1]
            
            
            if _left <= _right:
                return i+1
            
        
