class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = ['o' for i in range(1<<20)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.arr[self.myhash(key)]=value

    
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.arr[self.myhash(key)] == 'o':
            return -1 
        else:
            return self.arr[self.myhash(key)]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.arr[self.myhash(key)]='o'
    
        
        
    def myhash(self, key: int)->int:
        return (1031237*key & (1<<25)-1) >> 5


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
