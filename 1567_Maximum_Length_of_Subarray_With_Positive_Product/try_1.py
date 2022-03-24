class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = a = b = 0
        
        for num in nums:
            if num > 0:
                a, b = a + 1 if a > 0 else 1, b + 1 if b > 0 else 0
            elif num < 0:
                a, b = b + 1 if b > 0 else 0, a + 1 if a > 0 else 1
            else:
                a = b = 0
            
            ans = max(ans, a)
        
        return ans