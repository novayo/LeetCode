class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(i):
            cur_min = i
            left = i*2
            right = i*2+1

            if left < len(nums) and nums[left] < nums[cur_min]:
                cur_min = left

            if right < len(nums) and nums[right] < nums[cur_min]:
                cur_min = right

            if cur_min != i:
                nums[i], nums[cur_min] = nums[cur_min], nums[i]
                heapify(cur_min)
        
        def heapifyAll():
            for i in range(len(nums)//2, -1, -1):
                heapify(i)
        
        def pop():
            ret = nums[0]
            nums[0], nums[-1] = nums[-1], nums[0]
            nums.pop()
            heapify(0)
            return ret
        
        heapifyAll()
        
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            ans[i] = pop()
        return ans