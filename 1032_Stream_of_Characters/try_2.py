class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isWord = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.cur_search = ""
        self.root = Node()
        
        for word in words:
            root = self.root
            for w in word[::-1]:
                root = root.children[w]
            root.isWord = True

    def query(self, letter: str) -> bool:
        self.cur_search += letter
        if len(self.cur_search) > 200:
            self.cur_search = self.cur_search[1:]
        
        root = self.root
        for w in self.cur_search[::-1]:
            if w in root.children:
                root = root.children[w]
                if root.isWord:
                    return True
            else:
                return False
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
