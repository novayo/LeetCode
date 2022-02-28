class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def recr(nums):
            n = len(nums)
            
            if n <= 2:
                return sorted(nums)
            
            # divide
            left = recr(nums[:n//2])
            right = recr(nums[n//2:])
            
            # conquer
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
                i, l = i+1, l+1
            while r < len(right):
                nums[i] = right[r]
                i, r = i+1, r+1
            
            return nums
        
        return recr(nums)
