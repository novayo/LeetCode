class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quicksort(nums):
            if not nums:
                return []
            
            n = len(nums)
            pivot = random.randint(0, n-1)
            
            smaller = []
            bigger = []
            dups = []
            for k in range(0, n):
                if nums[k] < nums[pivot]:
                    smaller.append(nums[k])
                elif nums[k] > nums[pivot]:
                    bigger.append(nums[k])
                else:
                    dups.append(nums[k])
            
            return quicksort(smaller) + dups + quicksort(bigger)

        return quicksort(nums)
            