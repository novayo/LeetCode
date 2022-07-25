import bisect
import random
class Solution:

    def __init__(self, w: List[int]):
        _sum = sum(w)
        self.arr = [0]
        
        for _w in w:
            self.arr.append(self.arr[-1] + (_w / _sum))

    def pickIndex(self) -> int:
        pivot = random.random()
        i = bisect.bisect_left(self.arr, pivot) - 1
        return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
