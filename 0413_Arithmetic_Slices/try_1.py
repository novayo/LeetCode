class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''
        time complexity: O(n)
        space complexity: O(1)
        '''
        ans = 0
        i = 0
        while i <= len(nums)-3:
            cur_addition = 1
            j = i + 1
            cur_diff = nums[j] - nums[i]
            while j < len(nums):
                if nums[j] - nums[j-1] == cur_diff:
                    if j - i >= 2:
                        ans += cur_addition
                        cur_addition += 1
                    j += 1
                else:
                    break
            i = j - 1
        return ans