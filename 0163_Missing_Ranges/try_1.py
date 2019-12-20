class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if nums == []:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + "->" + str(upper)]
        ans = collections.deque()
        
        if lower == nums[0] - 1:
            ans.append(str(lower))
        elif lower < nums[0] - 1:
            ans.append(str(lower) + "->" + str(nums[0] - 1))
        
        pre = nums[0]
        for n in nums[1:]:
            if pre == n - 2:
                ans.append(str(n-1))
            elif pre < n - 2:
                ans.append(str(pre+1) + "->" + str(n-1))
            pre = n
        
        if nums[-1] == upper - 1:
            ans.append(str(upper))
        elif nums[-1] < upper - 1:
            ans.append(str(nums[-1] + 1) + "->" + str(upper))
        
        return ans
