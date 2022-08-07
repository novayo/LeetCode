from sortedcontainers import SortedList
class StockPrice:

    def __init__(self):
        self.cur = 0
        self.min_sd = SortedList()
        self.max_sd = SortedList()
        self.table = {}

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.table:
            ori_price = self.table[timestamp]
            self.min_sd.remove(ori_price)
            self.max_sd.remove(-ori_price)
        
        self.table[timestamp] = price
        self.min_sd.add(price)
        self.max_sd.add(-price)
        self.cur = max(self.cur, timestamp)

    def current(self) -> int:
        return self.table[self.cur]

    def maximum(self) -> int:
        return -self.max_sd[0]

    def minimum(self) -> int:
        return self.min_sd[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
