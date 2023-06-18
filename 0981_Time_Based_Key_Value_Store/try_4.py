class TimeMap:

    def __init__(self):
        self.table = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        j = bisect_right(self.table[key], [timestamp, "~"]) - 1
        if j >= 0:
            return self.table[key][j][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)