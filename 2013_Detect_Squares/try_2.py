import collections
class DetectSquares:

    def __init__(self):
        self.counter = collections.Counter()
        self.x_set = collections.defaultdict(set)
        self.y_set = collections.defaultdict(set)
        
    # O(1)
    def add(self, point: List[int]) -> None:
        x, y = point
        self.counter[x, y] += 1
        self.x_set[x].add((x, y))
        self.y_set[y].add((x, y))
        
    # O(n)
    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        for i, j in self.x_set[x]:
            dist = abs(y-j)
            
            if (i, j) == (x, y):
                continue
            
            if (x-dist, y) in self.counter and (x-dist, j) in self.counter:
                ans += self.counter[i, j] * self.counter[x-dist, y] * self.counter[x-dist, j]

            if (x+dist, y) in self.counter and (x+dist, j) in self.counter:
                ans += self.counter[i, j] * self.counter[x+dist, y] * self.counter[x+dist, j]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
