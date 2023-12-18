class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False
    
class Trie:
    # Space: O(26 ^ L)
    def __init__(self):
        self.root = Node()
    
    # O(L) - where L is the length of the input string
    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True

    # O(L) - where L is the length of the input string
    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            node = node.children.get(w)
            if node is None:
                return False
        return node.is_word

    # O(L) - where L is the length of the input string
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            node = node.children.get(w)
            if node is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
