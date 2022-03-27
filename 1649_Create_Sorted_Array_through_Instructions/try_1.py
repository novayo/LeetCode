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
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9+7
        
        # save memory
        index = {}
        for i, instruction in enumerate(sorted(list(set(instructions)))):
            index[instruction] = i+1
        
        # BIT
        tree = BIT(len(index))
        
        # get answer
        ans = 0
        for i, instruction in enumerate(instructions):
            ans += min(
                tree.query(index[instruction]-1),
                tree.query(len(index)) - tree.query(index[instruction])
            )
            ans = ans % MOD
            tree.update(index[instruction])
        return ans
