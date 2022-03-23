class DetectSquares:

    def __init__(self):
        self.all_nodes = collections.defaultdict(int)
        self.xs = collections.defaultdict(set)

    def add(self, point: List[int]) -> None:
        x, y = point
        
        self.all_nodes[x, y] += 1
        self.xs[x].add((x, y))
                
    def count(self, point: List[int]) -> int:
        ret = 0
        x, y = point
        
        y_set = self.xs[x]
        
        # ax = x
        for ax, ay in y_set:
            if (ax, ay) == (x, y):
                continue
                
            dist = abs(y-ay)
            b1x, b1y = x-dist, y
            b2x, b2y = x+dist, y
            
            if (b1x, b1y) in self.all_nodes and (b1x, ay) in self.all_nodes:
                ret += self.all_nodes[ax, ay] *\
                       self.all_nodes[b1x, b1y] *\
                       self.all_nodes[b1x, ay] 
            
            if (b2x, b2y) in self.all_nodes and (b2x, ay) in self.all_nodes:
                ret += self.all_nodes[ax, ay] *\
                       self.all_nodes[b2x, b2y] *\
                       self.all_nodes[b2x, ay]
            
        return ret

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)