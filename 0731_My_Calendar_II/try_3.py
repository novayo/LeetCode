class MyCalendarTwo:

    def __init__(self):
        self.cache = collections.Counter()

    def book(self, start: int, end: int) -> bool:
        self.cache[start] += 1
        self.cache[end] -= 1
        
        cur = 0
        for time in sorted(self.cache.keys()):
            cur += self.cache[time]
            if cur > 2:
                self.cache[start] -= 1
                self.cache[end] += 1
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)