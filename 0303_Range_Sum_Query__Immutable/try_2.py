class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = [0]
        for num in nums:
            self.presum.append(self.presum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right+1] - self.presum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
