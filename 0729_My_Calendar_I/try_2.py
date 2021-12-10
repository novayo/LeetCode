class MyCalendar:

    def __init__(self):
        self.list = []

    def book(self, start: int, end: int) -> bool:
        index1 = bisect.bisect_right(self.list, start)
        index2 = bisect.bisect_left(self.list, end)
        
        if index1 % 2 != 0 or index1 != index2:
            return False
        
        self.list[index1:index1] = [end]
        self.list[index1:index1] = [start]
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
