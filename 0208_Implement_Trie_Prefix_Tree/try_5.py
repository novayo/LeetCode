class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        ptr = self.root
        for w in word:
            if w not in ptr:
                ptr[w] = {'is_word': False}
            ptr = ptr[w]
        ptr['is_word'] = True
            
    def search(self, word: str) -> bool:
        ptr = self.root
        for w in word:
            if w not in ptr:
                return False
            ptr = ptr[w]
        return ptr['is_word']

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for w in prefix:
            if w not in ptr:
                return False
            ptr = ptr[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
