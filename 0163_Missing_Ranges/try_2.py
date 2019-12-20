class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = collections.deque()
        nums.append(upper+1)
        pre = lower-1
        
        for n in nums:
            if n == pre+2:
                ans.append(str(n-1))
            elif n > pre+2:
                ans.append(str(pre+1) + "->" + str(n-1))
            pre = n
        return ans
