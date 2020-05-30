class StockSpanner:

    def __init__(self):
        self.list = []

    def next(self, price: int) -> int:
        i = j = len(self.list)
        while True:
            j -= 1
            if j < 0 or self.list[j][1] > price:
                self.list.append((j+1, price))
                return i-j
            else:
                j = self.list[j][0]
            
        
         
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
