class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        ret = val not in self.dict
        if ret:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1
        return ret

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        ret = val in self.dict
        if ret:
            removedIndex = self.dict[val]
            self.list[removedIndex], self.list[-1] = self.list[-1], self.list[removedIndex]
            self.dict[self.list[removedIndex]] = removedIndex
            self.list.pop()
            del self.dict[val]
        return ret
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()