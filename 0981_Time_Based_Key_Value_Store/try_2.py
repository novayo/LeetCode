class TimeMap:

    def __init__(self):
        self.key_timestamp = {}
        self.timestamp_key_value = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_timestamp:
            self.key_timestamp[key] = []
        
        self.key_timestamp[key].append(timestamp)
        
        
        if timestamp not in self.timestamp_key_value:
            self.timestamp_key_value[timestamp] = {}
            
        self.timestamp_key_value[timestamp][key] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_timestamp:
            return ""
        
        
        index_in_timestamp = bisect.bisect_right(self.key_timestamp[key], timestamp) - 1
        
        time = self.key_timestamp[key][index_in_timestamp]
        if time > timestamp:
            return ""
        else:
            return self.timestamp_key_value[time][key]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
