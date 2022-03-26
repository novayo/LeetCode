class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            if candidate == num:
                count += 1
            elif count == 0:
                candidate = num
                count = 1
            else:
                count -= 1
        
        count = 0
        for num in nums:
            count += 1 if num == candidate else 0
        
        return candidate if count > len(nums)/2 else -1
