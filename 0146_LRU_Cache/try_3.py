class LRUCache:

    def __init__(self, capacity: int):
        self.dict = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
            
        self.dict.move_to_end(key)
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict[key] = value
            self.dict.move_to_end(key)
        elif len(self.dict) < self.capacity:
            self.dict[key] = value
        else:
            self.dict.popitem(last=False)
            self.dict[key] = value
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
