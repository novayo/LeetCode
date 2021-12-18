class Solution:

    def __init__(self, w: List[int]):
        self.presum = [w[0]]
        for _w in w[1:]:
            self.presum.append(self.presum[-1] + _w)
            
        
    def pickIndex(self) -> int:
        target = random.randint(0, self.presum[-1]-1)
        index = bisect.bisect_right(self.presum, target)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
