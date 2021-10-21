class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ordereddict = collections.OrderedDict()

    def get(self, key: int) -> int:
        value = self.ordereddict.get(key, -1)
        
        # if hit => move to the end
        if value > -1:
            del self.ordereddict[key]
            self.ordereddict[key] = value
        
        return value

    def put(self, key: int, value: int) -> None:
        # if hit => move to the end
        if key in self.ordereddict:
            del self.ordereddict[key]
            self.ordereddict[key] = value # move to end
        else:
            # if not hit => if over size => delete the first item in dict(least recently used key)
            if len(self.ordereddict) >= self.capacity:
                self.ordereddict.popitem(last=False)
            self.ordereddict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)