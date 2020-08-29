class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointer
        '''
        right往右，如果遇到不為0，與left交換後，left往前到下一個0的位置，
        （如果left > right，則要將right更新到left）
        如果right找到底代表已經沒有可以換的了，直接break
        '''
        left = right = 0
        while right < len(nums):
            # 移動left，移動到下一個0
            while left < len(nums) and nums[left] != 0:
                left += 1
            
            if left > right:
                right = left
                
            # 移動right，移動到下一個非0
            while right < len(nums) and nums[right] == 0:
                right += 1
            
            if right >= len(nums):
                return
            else:
                nums[left], nums[right] = nums[right], nums[left]
            
