class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()
        self.table = collections.defaultdict(int)
        self.total = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.set.add(timestamp)
        self.table[timestamp] += 1
        self.total += 1
        
        tmp = min(self.set)
        while timestamp - tmp >= 300:
            self.total -= self.table[tmp]
            self.table[tmp] = 0
            self.set.remove(tmp)
            tmp = min(self.set)
        
    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if len(self.set) > 0: 
            tmp = min(self.set)
            while timestamp - tmp >= 300:
                self.total -= self.table[tmp]
                self.table[tmp] = 0
                self.set.remove(tmp)
                if len(self.set) > 0:
                    tmp = min(self.set)
                else:
                    break
        return self.total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
