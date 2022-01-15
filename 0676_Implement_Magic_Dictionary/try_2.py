'''
Trie
mask
'''

class Node:
    def __init__(self, w=None):
        self.w = w
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        root = self.root
        for w in word:
            if w not in root.children:
                root.children[w] = Node(w)
            root = root.children[w]
        root.isWord = True
    
    def search(self, word):
        root = self.root
        for w in word:
            if w not in root.children:
                return False
            root = root.children[w]
        return root.isWord
                
        
class MagicDictionary:

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        root = self.trie.root
        
        def dfs(index, root, changed):
            
            if index >= len(searchWord):
                return changed and root.isWord
            
            word = searchWord[index]
            
            if not changed:
                # don't changed
                if word in root.children and dfs(index+1, root.children[word], changed):
                    return True
                
                # change
                for child in root.children.keys():
                    if child != word and dfs(index+1, root.children[child], not changed):
                        return True
            else:
                # don't changed
                if word in root.children and dfs(index+1, root.children[word], changed):
                    return True
        
        return dfs(0, root, False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
