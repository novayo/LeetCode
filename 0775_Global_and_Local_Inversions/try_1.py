class BIT:
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
    def isIdealPermutation(self, nums: List[int]) -> bool:
        '''
        find global => O(n)
        global => 找右邊有幾個人比我小 => 最後再sum起來算總個數
            => bit
            
        find local => O(n)
        local => 相鄰兩個，左邊大於右邊
            => 直接數
        '''
        n = len(nums)
        _local = _global = 0
        
        # find local
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                _local += 1
        
        # find global
        tree = BIT(n)
        for i in range(n-1, -1, -1):
            _global += tree.query(nums[i])
            
            if _global > _local:
                return False
            
            tree.update(nums[i]+1)
        return _global == _local
        
        
