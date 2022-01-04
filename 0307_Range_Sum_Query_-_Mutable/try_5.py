class Binary_Index_Tree:
    def __init__(self, nums):
        self.arr = [0] * (len(nums)+1)
        self.build(nums)
    
    def build(self, nums):
        for i, num in enumerate(nums):
            self.update(i+1, num)
    
    def update(self, index, delta):
        while index < len(self.arr):
            self.arr[index] += delta
            index += (index & -index)

    def query(self, index):
        val = 0
        while index > 0:
            val += self.arr[index]
            index -= (index & -index)
        return val
            
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = Binary_Index_Tree(nums)

    def update(self, index: int, val: int) -> None:
        self.bit.update(index+1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.query(right+1) - self.bit.query(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)