class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        found = set()
        
        tmp = tuple(nums)
        while tmp not in found:
            found.add(tmp)
            ans.append(nums.copy())
            self.next_permutation(nums)
            tmp = tuple(nums)
        return ans
    
    def next_permutation(self, nums):
        '''
        nums: pass by reference
        '''
        l = len(nums)-1
        # find lower
        while l > 0 and nums[l-1] >= nums[l]:
            l -= 1
        l -= 1
        
        # find bigger
        r = l+1
        while r < len(nums) and nums[l] <= nums[r]:
            r += 1
        r -= 1
        
        # swap
        nums[l], nums[r] = nums[r], nums[l]
        
        # reverse
        nums[l+1:] = reversed(nums[l+1:])
