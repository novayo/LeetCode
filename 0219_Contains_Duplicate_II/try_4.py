class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = collections.Counter()
        i = 0
        for j, num in enumerate(nums):
            if j-i > k:
                counter[nums[i]] -= 1
                i += 1

            counter[num] += 1
            if counter[num] > 1:
                return True
        return False