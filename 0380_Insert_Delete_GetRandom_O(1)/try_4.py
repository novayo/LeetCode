class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        
        self.index_map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        
        index = self.index_map[val] # 目標值
        end_index = len(self.arr)-1 # 最後一個值

        self.index_map[self.arr[end_index]] = index # 先變更最後一個值的index到目標index (防止目標即為最後一個值，刪除會有問題)
        del self.index_map[val] # 刪除紀錄值

        self.arr[index], self.arr[end_index] = self.arr[end_index], self.arr[index] # 目標值跟最後一個交換
        self.arr.pop() # 刪除目標值
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()