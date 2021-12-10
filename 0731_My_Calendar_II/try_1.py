class MyCalendarTwo:

    def __init__(self):
        self.table = collections.defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        if len(self.table) == 0:
            self.table[start] += 1
            self.table[end] -= 1
            return True
        
        self.table[start] += 1
        self.table[end] -= 1
        
        key_list = sorted(self.table.keys())
        cur_sum = 0
        for key in key_list:
            cur_sum += self.table[key]
            if cur_sum > 2:
                self.table[start] -= 1
                self.table[end] += 1
                return False
        
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
