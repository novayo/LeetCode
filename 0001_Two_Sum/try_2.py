class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # https://leetcode.com/problems/two-sum/submissions/
        hash_table = {}
        for i in range(0,len(nums)):
            if hash_table.get(target - nums[i]) is not None:
                return hash_table[target - nums[i]], i
            hash_table[nums[i]] = i
