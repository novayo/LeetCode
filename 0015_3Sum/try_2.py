class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        固定一個，轉成two sum
        time complexity: O(n^2)
        '''
        nums.sort()
        ret = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
                
            if i == 0 or nums[i] != nums[i-1]:
                found = set()
                for j in range(i+1, len(nums)):
                    if -nums[i] - nums[j] in found:
                        ret.add(tuple(sorted([nums[i], -nums[i] - nums[j], nums[j]])))
                    else:
                        found.add(nums[j])
        
        return list(ret)
