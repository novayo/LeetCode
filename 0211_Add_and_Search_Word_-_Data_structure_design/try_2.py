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
        queue.append((self.root, 0))
        
        while queue:
            node, index = queue.pop()
            if index == len(word):
                if node.finish:
                    return True
            elif word[index] == '.':
                for k in node.children.values():
                    queue.append((k, index+1))
            else:
                node = node.children.get(word[index])
                if node:
                    queue.append((node, index+1))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
