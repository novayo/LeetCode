class BIT:
    def __init__(self, n):
        self.arr = [0] * (n+1)
    
    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.arr[i]
            i -= (i & -i)
        return ret
    
    def update(self, i, delta):
        while i < len(self.arr):
            self.arr[i] += delta
            i += (i & -i)

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = BIT(len(nums))
        
        for i in range(len(nums)):
            self.tree.update(i+1, nums[i])

    def update(self, index: int, val: int) -> None:
        self.tree.update(index+1, val - self.nums[index])
        self.nums[index] = val
    
    
    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(right+1) - self.tree.query(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
