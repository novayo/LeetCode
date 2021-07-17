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

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # 必須由小到大排序，並取得index
        index_table = {}
        for i, num in enumerate(sorted(set(nums))):
            index_table[num] = i+1 # index 不能從0開始(因為bit運算)
        
        ans = collections.deque()
        tree = BIT(len(nums))
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            index = index_table[num]
            ans.appendleft(tree.query(index - 1))
            tree.update(index, 1)
        return ans
            
