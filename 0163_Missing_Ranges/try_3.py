class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        '''
        O(n) time / O(n) space
        
        nums may be empty
        
        start => min(nums[0], lower)
        end => max(nums[-1], lower)
        
        for num in nums:
            if start < num:
                update(start -> num-1)
            start = num+1
        
        if start <= end:
            update(start -> end)
        '''
        def update(a, b):
            if a != b:
                return f"{a}->{b}"
            else:
                return f"{a}"
        
        if not nums:
            return [update(lower, upper)]
        
        ans = []
        start = min(nums[0], lower)
        end = max(nums[-1], upper)
        
        for num in nums:
            if start < num:
                ans.append(update(start, num-1))
            start = num + 1
        
        if start <= end:
            ans.append(update(start, end))
        
        return ans
