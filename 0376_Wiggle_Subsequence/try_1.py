class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = []
        start = 0
        while len(dp) < 2 and start < len(nums):
            if not dp:
                dp.append(nums[start])
            elif dp[-1] != nums[start]:
                dp.append(nums[start])
            start += 1
        
        for num in nums[start:]:
            if (dp[-1] > dp[-2] and dp[-1] > num) or (dp[-1] < dp[-2] and dp[-1] < num):
                dp.append(num)
            else:
                dp[-1] = num
        
        return len(dp)