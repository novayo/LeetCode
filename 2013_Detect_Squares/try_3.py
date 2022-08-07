class DetectSquares:

    def __init__(self):
        self.xs = collections.defaultdict(set)
        self.ys = collections.defaultdict(set)
        self.counter = collections.Counter()

    def add(self, point: List[int]) -> None:
        x, y = point
        t_point = tuple(point)
        self.xs[x].add(t_point)
        self.ys[y].add(t_point)
        self.counter[t_point] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        t_point = tuple(point)
        
        ans = 0
        for _, j in self.xs[x]:
            if (x, j) == t_point:
                continue
            dist = j-y
            p2 = (x, j)
            p3 = (x+dist, y)
            p4 = (p3[0], p2[1])
            ans += self.counter[p2] * self.counter[p3] * self.counter[p4]
            
            p3 = (x-dist, y)
            p4 = (p3[0], p2[1])
            ans += self.counter[p2] * self.counter[p3] * self.counter[p4]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
