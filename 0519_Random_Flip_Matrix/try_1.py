class Solution:

    def __init__(self, m: int, n: int):
        self.total = m*n-1
        self.end = self.total
        self.n = n
        self.table = {}

    def flip(self) -> List[int]:
        i = random.randint(0, self.end)
        
        val = self.table.get(i, i)
        self.table[i] = self.table.get(self.end, self.end)
        self.end -= 1
        return val // self.n, val % self.n

    def reset(self) -> None:
        self.end = self.total
        self.table = {}


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
