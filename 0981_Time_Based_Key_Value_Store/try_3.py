class TimeMap:

    def __init__(self):
        self.table = collections.defaultdict(list)
        
        '''
        dict1 = {key: [(timestamp, value)]}
        '''
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""
        
        
        # bisect right
        index = -1
        l, r = 0, len(self.table[key])-1
        while l <= r:
            mid = l + (r-l) // 2
            if self.table[key][mid][0] == timestamp:
                return self.table[key][mid][1]
            elif self.table[key][mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        index = l - 1
        
        time, value = self.table[key][index]
        if time > timestamp:
            return ""
        else:
            return value


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
