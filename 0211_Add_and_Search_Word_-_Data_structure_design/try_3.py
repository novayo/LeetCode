class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    # O(L) - where L is the length of the input string
    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True

    # O(L + 26^2) - where L is the length of the input string
    def search(self, word: str) -> bool:
        def recr(idx, node):
            if node is None:
                return False

            if idx >= len(word):
                return node.is_word
            
            w = word[idx]
            if w == '.':
                for child in node.children.values():
                    if recr(idx+1, child):
                        return True
            else:
                if w in node.children and recr(idx+1, node.children[w]):
                    return True
            return False
        
        return recr(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
