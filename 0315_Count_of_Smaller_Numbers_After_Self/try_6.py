class BIT:
    def __init__(self, n):
        self.arr = [0] * (n+1)
    
    def update(self, idx, delta=1):
        while idx < len(self.arr):
            self.arr[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        ret = 0
        while idx > 0:
            ret += self.arr[idx]
            idx -= idx & -idx
        return ret

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # reorg input array
        n = len(nums)
        _min = min(nums)
        for i in range(n):
            if _min >= 0:
                nums[i] += _min
            else:
                nums[i] -= _min
        
        # get ans
        ans = []
        tree = BIT(2*(10**4))
        for num in nums[::-1]:
            ans.append(tree.query(num))
            tree.update(num+1)
        return ans[::-1]
        
