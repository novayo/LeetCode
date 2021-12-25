class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = candidate2 = None
        count1 = count2 = 0
        
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        ans = set()
        count1 = count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            if num == candidate2:
                count2 += 1
        
        if count1 > len(nums) / 3:
            ans.add(candidate1)
        if count2 > len(nums) / 3:
            ans.add(candidate2)
        
        return list(ans)
