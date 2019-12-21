class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.finish = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for w in word:
            node = node.children[w]
        node.finish = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        queue = collections.deque()
        queue.append((self.root, word))
        
        while queue:
            node, nodeWord = queue.pop()
            if nodeWord == '':
                return node.finish
            for i, w in enumerate(nodeWord):
                if w == '.':
                    for k in node.children.values():
                        queue.append((k, nodeWord[i+1:]))
                    break
                else:
                    node = node.children.get(w)
                    if node:
                        queue.append((node, nodeWord[i+1:]))
                    else:
                        break
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
