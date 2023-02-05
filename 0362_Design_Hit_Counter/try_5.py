class HitCounter:

    def __init__(self):
        self.history = []

    def hit(self, timestamp: int) -> None:
        self.history.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        r = bisect.bisect_right(self.history, timestamp)-1
        l = bisect.bisect_right(self.history, timestamp-300)-1
        return r-l


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
