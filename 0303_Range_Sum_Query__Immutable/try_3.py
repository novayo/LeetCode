class NumArray:
    # O(1) / O(n)
    def __init__(self, nums: List[int]):
        self.nums = nums

    # O(n)
    def sumRange(self, left: int, right: int) -> int:
        _sum = 0
        for i in range(left, right+1):
            _sum += self.nums[i]
        return _sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
