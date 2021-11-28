class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        bucket sort => num as bucket
        '''
        
        bucket = set()
        
        for num in nums:
            if num in bucket:
                return True
            else:
                bucket.add(num)
                
        return False
        
