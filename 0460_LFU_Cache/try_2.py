from collections import OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.counter_dict = {}
        self.mapping_dict = {}
        self.last_freq = 0
        self.capacity = capacity

    def _update(self, key, value):
        current_freq = self.mapping_dict[key]
        next_freq = current_freq+1

        # pop from old counter
        del self.counter_dict[current_freq][key]
        if len(self.counter_dict[current_freq]) == 0:
            del self.counter_dict[current_freq]

            # update last freq
            if current_freq == self.last_freq:
                self.last_freq = next_freq
        
        # add to new counter
        if next_freq not in self.counter_dict:
            self.counter_dict[next_freq] = OrderedDict()
        self.counter_dict[next_freq][key] = value
        
        # update mapping dict
        self.mapping_dict[key] = next_freq
        
    def get(self, key: int) -> int:
        if self.capacity == 0:
            return -1

        if key not in self.mapping_dict:
            return -1
        
        val = self.counter_dict[self.mapping_dict[key]][key]
        self._update(key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key not in self.mapping_dict:
            if len(self.mapping_dict) >= self.capacity:
                k, v = self.counter_dict[self.last_freq].popitem(last=False)
                del self.mapping_dict[k]
            
            self.last_freq = 1
            self.mapping_dict[key] = 1
            if 1 not in self.counter_dict:
                self.counter_dict[1] = OrderedDict()
            self.counter_dict[1][key] = value
        else:
            self._update(key, value)
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

