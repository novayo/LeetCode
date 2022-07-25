class MyCalendar:

    def __init__(self):
        self.table = collections.defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.table[start] += 1
        self.table[end] -= 1
        
        cur = 0
        for k in sorted(self.table.keys()):
            cur += self.table[k]
            
            if cur > 1:
                self.table[start] -= 1
                self.table[end] += 1
                return False
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
