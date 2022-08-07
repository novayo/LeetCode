class Solution:

    def __init__(self, w: List[int]):
        _sum = sum(w)
        self.portion = [0]
        for _w in w:
            self.portion.append(self.portion[-1] + (_w/_sum))

    def pickIndex(self) -> int:
        pivot = random.random()
        return bisect.bisect_left(self.portion, pivot) - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
