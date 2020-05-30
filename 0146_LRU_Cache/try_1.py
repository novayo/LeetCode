class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.queue = collections.deque()

    def get(self, key: int) -> int:
        ret = self.dict.get(key, -1)
        if ret == -1:
            return -1
        else:
            self.queue.remove(key) # O(n)
            self.queue.appendleft(key)
            # print(self.queue)
            return ret

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            self.dict[key] = value
        
        
            if len(self.queue) == self.capacity:
                tmp = self.queue.pop()
                del self.dict[tmp]

            self.queue.appendleft(key)
        else:
            self.dict[key] = value
            self.queue.remove(key) # O(n)
            self.queue.appendleft(key)
        # print(self.queue)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
