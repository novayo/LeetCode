class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        O(n) O(1)
        
        將原本的list轉成set
        之後從0開始往上加即可
        '''
        
        nums = set(nums)
        
        i = 0
        while True:
            if i in nums:
                i += 1
            else:
                return i
