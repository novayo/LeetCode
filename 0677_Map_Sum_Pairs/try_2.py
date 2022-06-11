class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.sum = 0
        self.isWord = False

class MapSum:

    def __init__(self):
        self.cache = collections.defaultdict(int)
        self.root = Node()

    def insert(self, key: str, val: int) -> None:
        diff = val - self.cache[key]
        
        root = self.root
        for w in key:
            root = root.children[w]
            root.sum += diff
        root.isWord = True
        self.cache[key] = val

    def sum(self, prefix: str) -> int:
        root = self.root
        for w in prefix:
            root = root.children[w]
        return root.sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)