'''
list + set
'''

class RandomizedSet:

    def __init__(self):
        self.table = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.table:
            return False
        
        self.table[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.table:
            return False
        
        val_index, swap_index = self.table[val], len(self.array)-1
        
        self.table[self.array[swap_index]] = val_index
        self.array[val_index], self.array[swap_index] = self.array[swap_index], self.array[val_index]
        
        del self.table[val]
        self.array.pop()
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
