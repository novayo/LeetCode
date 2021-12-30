class Node:
    def __init__(self, w):
        self.w = w
        self.children = collections.defaultdict(Node)
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = Node('#')

    def insert(self, word: str) -> None:
        node = self.root
        
        for w in word:
            if w not in node.children:
                node.children[w] = Node(w)
            node = node.children[w]
        
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        
        for w in word:
            if w not in node.children:
                return False
            else:
                node = node.children[w]
        
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for w in prefix:
            if w not in node.children:
                return False
            else:
                node = node.children[w]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
