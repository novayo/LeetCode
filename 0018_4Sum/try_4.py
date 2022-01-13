class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.ksum(nums, target, 4)
    
    def ksum(self, nums, target, k):
        if k == 2:
            ans = set()
            found = set()
            for num in nums:
                if target - num in found:
                    if num <= target-num:
                        ans.add((num, target-num))
                    else:
                        ans.add((target-num, num))
                found.add(num)
            return ans
        else:
            ret = set()
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for _list in self.ksum(nums[i+1:], target-nums[i], k-1):
                        tmp = tuple(sorted([nums[i]] + list(_list)))
                        ret.add(tmp)
            return ret
