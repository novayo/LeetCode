class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Kth smallest
        def quick_select(l, r, target):
            pivot_index = random.randint(l, r)
            nums[r], nums[pivot_index] = nums[pivot_index], nums[r]
            
            i = l
            for j in range(l, r):
                if nums[j] < nums[r]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            
            if i == target:
                return nums[i]
            elif i > target:
                return quick_select(l, i-1, target)
            else:
                return quick_select(i+1, r, target)
            
        return quick_select(0, len(nums)-1, len(nums)-k)
