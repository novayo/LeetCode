class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        bucket sort => num as key
        '''
        
        bucket = set()
        
        for i in range(len(nums)):
            if nums[i] in bucket:
                return True
            
            bucket.add(nums[i])
            if i >= k:
                bucket.remove(nums[i-k])
        
        return False
        
