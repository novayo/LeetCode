class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        讓index為value的位置變成-的，之後檢查-的即可
        
        1. 先查看是否答案是1
        2. 將超過範圍的值改成1 (1~len(nums)-1)
        3. 將對應value的index改成負的
        4. loop第一個正的
        '''
        n = len(nums)
        
        # 1, 2
        exist_1 = False
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 1
            elif nums[i] == 1:
                exist_1 = True
        
        if not exist_1:
            return 1
        
        # 3
        i = 0
        while i < n:
            j = abs(nums[i])-1
            nums[j] = -abs(nums[j])
            i += 1
        
        # 4
        for i in range(n):
            if nums[i] > 0:
                return i+1
        
        return n+1
