class Binary_Index_Tree:
    def __init__(self, arr_length):
        self.length = arr_length + 1
        self.arr = [0] * self.length
    
    def update(self, index, delta):
        while index < self.length:
            self.arr[index] += delta
            index += self.lower_bit(index)
    
    def sum_of_0_to_index(self, index):
        sum = 0
        while index > 0:
            sum += self.arr[index]
            index -= self.lower_bit(index)
        return sum
    
    def lower_bit(self, index):
        return index & -index
        
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.arr = Binary_Index_Tree(len(nums))
        
        # init - O(nlogn)
        for i in range(len(nums)):
            self.arr.update(i + 1, nums[i])

    def update(self, index: int, val: int) -> None:
        # O(logn)
        delta = val - self.nums[index]
        self.nums[index] = val # 要更新nums才能計算下一次的delta
        self.arr.update(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        # O(logn)
        return self.arr.sum_of_0_to_index(right + 1) - self.arr.sum_of_0_to_index(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)