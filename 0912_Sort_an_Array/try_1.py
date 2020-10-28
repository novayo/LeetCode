class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        top-down merge sort
        '''
        if len(nums) <= 1:
            return nums
        
        pivot = len(nums) // 2
        left = self.sortArray(nums[0:pivot])
        right = self.sortArray(nums[pivot:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        ret = []
        left_index = right_index = 0
        
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                ret.append(left[left_index])
                left_index += 1
            else:
                ret.append(right[right_index])
                right_index += 1
        
        ret.extend(left[left_index:])
        ret.extend(right[right_index:])
        return ret