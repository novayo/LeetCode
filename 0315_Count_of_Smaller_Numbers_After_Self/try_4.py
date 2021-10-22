class BIT:
    def __init__(self, n):
        self.arr = [0] * (n+1)
        
    def query(self, index):
        ret = 0
        while index > 0:
            ret += self.arr[index]
            index -= index & -index
        return ret
    
    def update(self, index, delta=1):
        while index < len(self.arr):
            self.arr[index] += delta
            index += index & -index

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        cur_max = 0
        cur_min = min(nums)
        for i in range(len(nums)):
            nums[i] -= cur_min-1
            cur_max = max(cur_max, nums[i])
        
        tree = BIT(cur_max)
        ans = []
        for num in nums[::-1]:
            bigger = tree.query(num-1)
            ans.append(bigger)
            tree.update(num)
        
        return ans[::-1]