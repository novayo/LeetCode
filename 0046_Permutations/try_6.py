class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        found = set()
        cur = tuple(nums)
        
        while cur not in found:
            ans.append(cur)
            found.add(cur)
            nums = self.next_permutation(nums)
            cur = tuple(nums)
        return ans
        
    
    def next_permutation(self, nums):
        i = j = len(nums)-1
        
        # [1.] 向左找到第一個非遞減的值
        while i > 0 and nums[i-1] > nums[i]:
            i -= 1
        i -= 1
        
        # [2.] 向右找到略大於[1]的值
        j = i + 1
        while j < len(nums) and nums[j] > nums[i]:
            j += 1
        j -= 1
        
        # [3.] 交換
        nums[i], nums[j] = nums[j], nums[i]
        
        # [4.] reverse
        nums[i+1:] = reversed(nums[i+1:])
        
        return nums
