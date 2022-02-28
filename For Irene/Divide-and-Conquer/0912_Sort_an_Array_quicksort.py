class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def recr(l, r):
            if l > r:
                return []
            pivot = random.randint(l, r)
            nums[pivot], nums[r] = nums[r], nums[pivot]
            
            i = l
            for j in range(l, r):
                if nums[j] < nums[r]:
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            
            return recr(l, i-1) + [nums[i]] + recr(i+1, r)
        
        return recr(0, len(nums)-1)
