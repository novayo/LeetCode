class HitCounter:

    def __init__(self):
        self.counter = 0
        self.history_timestamp = [0]
        self.history_counter = {0:0}
        
    def hit(self, timestamp: int) -> None:
        self.counter += 1
        
        if timestamp not in self.history_counter:
            self.history_timestamp.append(timestamp)
            self.history_counter[timestamp] = self.counter
        else:
            self.history_timestamp[-1] = timestamp
            self.history_counter[timestamp] = self.counter

    def getHits(self, timestamp: int) -> int:
        start = max(0, timestamp - 300)
        pre_index = bisect.bisect_right(self.history_timestamp, start)-1
        pre_timestamp = self.history_timestamp[pre_index]
        pre_counter = self.history_counter[pre_timestamp]
        
        index = bisect.bisect_right(self.history_timestamp, timestamp)-1
        end = self.history_timestamp[index]
        counter = self.history_counter[end]
        
        return counter - pre_counter

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)