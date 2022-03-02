class Node:
    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        root = self.root
        
        for w in word[:-1]:
            if w not in root.children:
                return False
            root = root.children[w]
        
        root = root.children[word[-1]]
        root.isWord = True
        return root.isWord

class Solution:
    def longestWord(self, words: List[str]) -> str:
        '''
        Build Trie & add into Trie by length order
        Get answer by length
        '''
        ans = ''
        words.sort(key=lambda x: (len(x), x))
        tree = Trie()
        for word in words:
            if tree.add(word):
                if len(word) > len(ans):
                    ans = word
        return ans