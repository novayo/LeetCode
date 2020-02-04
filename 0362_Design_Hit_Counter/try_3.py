class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = collections.defaultdict(int)
        self.sum = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.table[timestamp] += 1
        self.sum += 1
        
    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if len(self.table) > 0:
            for k, y in list(self.table.items()):
                if timestamp - k >= 300:
                    self.sum -= y
                    del self.table[k]
                if self.table and timestamp - min(self.table.keys()) < 300:
                    break
            return self.sum
        else:
            return 0

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
