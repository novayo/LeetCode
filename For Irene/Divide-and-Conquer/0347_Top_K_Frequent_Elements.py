class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        def quickselect(l, r, k):
            pivot_index = random.randint(l, r)
            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
            
            i = l
            for j in range(l, r):
                if counter[nums[j]] < counter[nums[r]]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            
            if i == k:
                return nums
            elif i > k:
                return quickselect(l, i-1, k)
            else:
                return quickselect(i+1, r, k)
        
        counter = collections.Counter(nums)
        nums = list(counter.keys())
        return quickselect(0, len(nums)-1, len(nums)-k)[-k:]
