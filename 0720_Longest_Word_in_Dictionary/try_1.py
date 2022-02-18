class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        root = self.root
        for i, w in enumerate(word):
            if w not in root.children and i+1 < len(word):
                return False
                
            root = root.children[w]
        root.isWord = True
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        '''
        sort and build Trie
        '''
        ans = ''
        tree = Trie()
        
        words.sort()
        for word in words:
            if tree.add(word):
                if len(ans) < len(word):
                    ans = word
        return ans
        