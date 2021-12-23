class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.list = []

    def seat(self) -> int:
        seat = 0
        if self.list:
            dist = self.list[0] - 0
            
            for i in range(1, len(self.list)):
                a, b = self.list[i-1], self.list[i]
                
                if (b-a)//2 > dist:
                    dist = (b-a)//2
                    seat = (b+a)//2
            
            if self.n-self.list[-1]-1 > dist:
                seat = self.n-1
        
        index = bisect.bisect_left(self.list, seat)
        self.list[index:index] = [seat]
        
        return seat

    def leave(self, p: int) -> None:
        index = bisect.bisect_left(self.list, p)
        del self.list[index]


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
