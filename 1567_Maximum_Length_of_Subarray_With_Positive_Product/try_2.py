class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for num in nums:
            if num > 0:
                pos = pos+1
                neg = neg+1 if neg > 0 else 0
            elif num == 0:
                pos = neg = 0
            else:
                tmp = pos
                pos = neg+1 if neg > 0 else 0
                neg = tmp+1
            
            ans = max(ans, pos)
        return ans
