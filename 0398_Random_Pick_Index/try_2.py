class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ret = count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.random() < 1/count:
                    ret = i
        return ret


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)