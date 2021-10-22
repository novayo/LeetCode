class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def recr(nums):
            n = len(nums)
            
            if n <= 2:
                nums.sort()
                return nums
            
            
            left = recr(nums[:n//2])
            right = recr(nums[n//2:])
            
            i = l = r = 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    nums[i] = left[l]
                    l += 1
                else:
                    nums[i] = right[r]
                    r += 1
                i += 1
            
            while l < len(left):
                nums[i] = left[l]
                l += 1
                i += 1
            
            while r < len(right):
                nums[i] = right[r]
                r += 1
                i += 1
            
            return nums
    
        return recr(nums)