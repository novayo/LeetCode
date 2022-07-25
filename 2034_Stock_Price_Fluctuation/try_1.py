'''
每個時間點的price

current => last timestamp value
maximum => max
minimum => min

'''

# ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
# [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
# Output
# [null, null, null, 5, 10, null, 5, null, 2]

from sortedcontainers import SortedList

class StockPrice:

    def __init__(self):
        self.bst = SortedList()
        self.d = {}
        self.cur = -1

    # O(logn) time
    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.d:
            self.bst.remove(self.d[timestamp])
        
        self.bst.add(price)
        self.d[timestamp] = price
        self.cur = max(self.cur, timestamp)

    # O(1) time
    def current(self) -> int:
        return self.d[self.cur]

    # O(logn) time
    def maximum(self) -> int:
        return self.bst[-1]

    # O(logn) time
    def minimum(self) -> int:
        return self.bst[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
