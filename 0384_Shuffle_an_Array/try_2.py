class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums.copy()
        self.nums = nums

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        index_1 = random.randint(0, len(self.nums)-1)
        index_2 = random.randint(0, len(self.nums)-1)
        self.nums[index_1], self.nums[index_2] = self.nums[index_2], self.nums[index_1]
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
