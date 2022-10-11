class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for index, value in enumerate(nums):
            if target - value in hash_table: # O(1)
                return [hash_table[target - value], index]
            hash_table[value] = index
