class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [[] for _ in range(1<<15)]

    def add(self, key: int) -> None:
        hashed = self.myHash(key)
        if self.contains(key) == False:
            self.arr[hashed].append(key)
        
    def remove(self, key: int) -> None:
        hashed = self.myHash(key)
        if self.contains(key) == True:
            self.arr[hashed].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashed = self.myHash(key)
        return key in self.arr[hashed]
        
    def myHash(self, key: int) -> int:
        return ((key*1031237) & 1<<20-1) >> 5

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)