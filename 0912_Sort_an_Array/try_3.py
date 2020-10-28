class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        quicksort
        '''
        
        if len(nums) <= 1:
            return nums

        pivot = nums[0]
        less = []
        equal = 0
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal += 1
            else:
                greater.append(num)

        return self.sortArray(less) + [pivot] * equal + self.sortArray(greater)