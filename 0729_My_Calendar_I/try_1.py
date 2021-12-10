class MyCalendar:

    def __init__(self):
        self.table = {}

    def book(self, start: int, end: int) -> bool:
        if not self.table:
            self.table[start] = end
            return True
        
        key_list = sorted(self.table.keys())
        
        index = max(bisect.bisect_right(key_list, start)-1, 0)

        pre_start = key_list[index]
        pre_end = self.table[pre_start]
        
        if start < pre_start:
            if end <= pre_start:
                self.table[start] = end
                return True
            else:
                return False
        else:
            if start >= pre_end:
                if index+1 >= len(key_list):
                    self.table[start] = end
                    return True
                else:
                    if end <= key_list[index+1]:
                        self.table[start] = end
                        return True
                    else:
                        return False
            else:
                return False
        
        
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
