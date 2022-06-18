class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.index_map = {}
        self.min_freq_idx = 0
        self.freqs = collections.defaultdict(lambda: collections.OrderedDict())
    
    # O(1)
    def update_freqs(self, key):
        idx = self.index_map[key]
        self.freqs[idx+1][key] = self.freqs[idx][key]
        self.index_map[key] += 1
        
        del self.freqs[idx][key]
        if idx == self.min_freq_idx and len(self.freqs[idx]) == 0:
            self.min_freq_idx += 1
    
    # O(1)
    def get(self, key: int) -> int:
        if key in self.index_map:
            self.update_freqs(key)
            return self.freqs[self.index_map[key]][key]
        return -1    
        
    # O(1)
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        # old
        if key in self.index_map:
            self.update_freqs(key)
            self.freqs[self.index_map[key]][key] = value
        
        # new
        else:
            # pop
            if len(self.index_map) + 1 > self.capacity:
                od = self.freqs[self.min_freq_idx]
                od_key, _  = od.popitem(last=False)
                del self.index_map[od_key]
            
            # add new element
            self.index_map[key] = 0
            self.freqs[0][key] = value
            self.min_freq_idx = 0


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)