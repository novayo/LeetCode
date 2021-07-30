class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
        self.sum = 0
        self.val = 0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, val):
        node_val = self.isWord(word)
        
        diff = val - node_val
        
        node = self.root
        for w in word:            
            node = node.children[w]
            node.val = val
            node.sum += diff
        node.isWord = True
    
    def query(self, word):
        node = self.root
        ret = 0
        
        for w in word:
            node = node.children[w]
            if not node:
                return 0
            ret = node.sum
        return ret
    
    def isWord(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return 0
        return node.val if node.isWord else 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.query(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
