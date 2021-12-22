class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        
        nums_set = set(nums)
        
        while nums_set:
            i = nums_set.pop()
            
            cur = 1
            j = i+1
            while j in nums_set:
                nums_set.remove(j)
                cur += 1
                j += 1
            
            k = i-1
            while k in nums_set:
                nums_set.remove(k)
                cur += 1
                k -= 1
            
            ans = max(ans, cur)
        
        return ans
        
