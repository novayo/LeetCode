class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        ans = 0
        max_attempt = 2**len(nums)-1
        slot_state_bitmask = max_slot = 0
        for i in range(numSlots):
            if any([num & (i+1) > 0 for num in nums]):
                max_slot |= (1<<(i*2+1))

        
        @functools.lru_cache(None)
        def recr(slot_state_bitmask, i):
            if slot_state_bitmask == max_slot or i >= len(nums):
                return 0
            
            ret = recr(slot_state_bitmask, i+1)
            for slot in range(numSlots):
                if slot_state_bitmask & (1 << (slot*2+1)) > 0:
                    continue
                    
                ret = max(
                    ret,
                    (nums[i] & (slot+1)) + recr(slot_state_bitmask + (1 << (slot*2)), i+1)
                )
            return ret
        
        return recr(slot_state_bitmask, 0)
        