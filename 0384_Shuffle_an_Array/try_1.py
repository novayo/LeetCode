class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.o_nums = nums.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.o_nums.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(0, len(self.nums)-1):
            index = random.randint(i, len(self.nums)-1)
            self.nums[i], self.nums[index] = self.nums[index], self.nums[i]
        
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
