class LogSystem:

    def __init__(self):
        self.sorted_time = []
        self.ids = []
        self.index = {
            'Year': 1,
            'Month': 2,
            'Day': 3,
            'Hour': 4,
            'Minute': 5,
            'Second': 6
        }

    def put(self, id: int, timestamp: str) -> None:
        index = bisect.bisect_left(self.sorted_time, timestamp)
        self.sorted_time[index: index] = [timestamp]
        self.ids[index: index] = [id]

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        start = start.split(':')
        end = end.split(':')

        for i in range(self.index[granularity], 6):
            start[i] = '00'
            end[i] = '59'
        
        index1 = bisect.bisect_left(self.sorted_time, ':'.join(start))
        index2 = bisect.bisect_right(self.sorted_time,':'.join(end))
        
        ans = []
        for i in range(index1, index2):
            ans.append(self.ids[i])
        return ans

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
