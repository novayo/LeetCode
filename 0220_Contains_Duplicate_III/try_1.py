class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        '''
        能否有一組 在index範圍為k的情況下，差距<=t，
        
        bucket sort => 用商當作bucket,
        
        if t == 3
        
        use t+1 to divide
        0: 0,1,2,3
        1: 4,5,6,7
        2: 8,9,10,11
        .
        .
        .
        
        
        故 在同一個bucket的都會滿足 "差距<=t"
        
        往後找每個元素，都去找說 是否有兩個在同一個籃子即可（題意）
        只是>=k時，要整理bucket
        
        因為bucket只需要一個數字，因此儲存int即可
        '''
        
        divisor = t+1
        buckets = {} # 因為值有負的，所以直接拿商當作key
        
        i = j = 0
        while j < len(nums):
            quotient = nums[j] // divisor
            
            # 有值跟自己同一層
            if quotient in buckets:
                return True
            
            # 有值在上一層，而且其值要跟自己差距在t內
            if quotient-1 in buckets and abs(buckets[quotient-1] - nums[j]) <= t:
                return True
            
            # 有值在下一層，而且其值要跟自己差距在t內
            if quotient+1 in buckets and abs(buckets[quotient+1] - nums[j]) <= t:
                return True
            
            buckets[quotient] = nums[j]
            if j - i >= k:
                del buckets[nums[i] // divisor]
                i += 1
                
            j += 1
        
        return False
