class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # set
        '''
        先紀錄長度，則範圍是1~len(nums)
        之後將nums轉成set
        
        for 1 ~ len(nums):
            如果在裡面，則刪除
            若不在裡面，則加入
        return list(nums)
        '''
        
        max_len = len(nums)
        nums = set(nums)
        for i in range(1, max_len+1):
            if i in nums:
                nums.remove(i)
            else:
                nums.add(i)
        return list(nums)
