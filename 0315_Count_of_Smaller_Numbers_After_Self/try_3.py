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
            self.arr[index] += 1
            index += index & -index

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        tmp = sorted(list(set(nums.copy())))
        
        index = {}
        for i in range(len(tmp)):
            index[tmp[i]] = i+1
        
        tree = BIT(len(tmp))
        ans = []
        for num in nums[::-1]:
            i = index[num]
            bigger = tree.query(i-1)
            ans.append(bigger)
            tree.update(i)
        
        return ans[::-1]