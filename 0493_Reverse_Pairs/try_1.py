class BIT():
    def __init__(self, n):
        self.arr = [0] * (n+1)
    
    def update(self, i, delta=1):
        while i < len(self.arr):
            self.arr[i] += delta
            i += i & -i
    
    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.arr[i]
            i -= i & -i
        return ret

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sorted_num = sorted(list(set(nums)))
        
        # mapping index
        index = {-float('inf'): 0}
        for i, num in enumerate(sorted_num):
            index[num] = i + 1
        
        # mapping value
        value = {}
        for num in sorted_num:
            i = bisect.bisect_right(sorted_num, ceil(num/2)-1) - 1
            if i == -1:
                value[num] = -float('inf')
            else:
                value[num] = sorted_num[i]
        
        # get answer
        ans = 0
        tree = BIT(len(index))
        
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            ans += tree.query(index[value[num]])
            tree.update(index[num])
        return ans
