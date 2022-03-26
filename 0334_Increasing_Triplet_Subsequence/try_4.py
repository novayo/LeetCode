class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # monotonic stack => find next bigger and pre smaller
        
        def getNextBigger(nums):
            next_bigger = [-float('inf')] * len(nums)
            min_stack = []
            for i, num in enumerate(nums):
                while min_stack and nums[min_stack[-1]] < num:
                    next_bigger[min_stack[-1]] = num
                    min_stack.pop()
                min_stack.append(i)
            return next_bigger
        
        def getPreSmaller(nums):
            next_smaller = [-float('inf')] * len(nums)
            max_stack = []
            for i in range(len(nums)-1, -1, -1):
                num = nums[i]
                while max_stack and nums[max_stack[-1]] > num:
                    next_smaller[max_stack[-1]] = num
                    max_stack.pop()
                max_stack.append(i)
            return next_smaller
        
        # find next bigger
        next_bigger = getNextBigger(nums)
        next_smaller = getPreSmaller(nums)
        
        
        
        # get answer
        for a, b in zip(next_bigger, next_smaller):
            if a > -float('inf') and b > -float('inf'):
                return True
        return False
