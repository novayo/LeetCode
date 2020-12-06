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
                left, right = i+1, len(nums)-1
                while left < right:
                    sum = nums[i] + nums[left] + nums[right]
                    if sum < 0:
                        left += 1
                    elif sum > 0:
                        right -= 1
                    else:
                        ret.add((nums[i], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
        
        return list(ret)