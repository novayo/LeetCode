class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        [1,2,3,4,5,6]
        [1,4,2,5,3,6]
        
        [1,2,3,4,5]
        [1,4,2,5,3]
        
        sort 後
        i = 1, j = len // 2 => i, j交換後，再讓i+1, j交換, i+=1, j+=1
        '''
        nums.sort()
        i, j = 1, math.ceil(len(nums) / 2)
        
        while j < len(nums) and i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
            i += 1

