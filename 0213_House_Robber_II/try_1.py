class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums.append(nums[0])
        if len(nums) <= 2:
            return max(nums)
        
        def find(nums):
            if len(nums) <= 2:
                return max(nums)
            
            heap = []
            for i in range(len(nums)-3, -1, -1):
                heapq.heappush(heap, -nums[i+2])
                nums[i] += -heap[0]

            return max(nums[0], nums[1])
        
        return max(find(nums[1:]), find(nums[:-1]))

