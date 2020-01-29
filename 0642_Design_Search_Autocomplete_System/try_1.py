class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
        self.word = ""

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, words):
        root = self.root
        for word in words:
            root = root.children[word]
        root.isWord = True
        root.word = words
    
    def search_char(self, preRoot, char):
        # search every char
        rt = collections.deque()
        root = self.root if preRoot == None else preRoot
        root = root.children.get(char)
        
        if root == None: # char not exist in trie
            return None, False
        elif len(root.children.keys()) == 0: # char is in trie and isWord but at the end of trie
            return None, [root.word]
        if root.isWord: # char is in trie and isWord but not at the end of trie
            rt.append(root.word)
        preRoot = root
        # get the autocomplete word
        queue = collections.deque()
        for children in root.children.values():
            queue.append(children)
            
        while queue:
            r = queue.popleft()
            if r.isWord:
                rt.append(r.word)
            for children in r.children.values():
                queue.append(children)
        return (preRoot, rt)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.sentences = sentences
        self.times = times
        self.pair = self.preprocess(self.sentences, self.times)
        self.cur_input = ""
        self.preRoot = None
        self.notaword = False # for the wrong word but still input

    def input(self, c: str) -> List[str]:
        self.cur_input += c
        if c == "#":
            self.cur_input = self.cur_input[:-1]
            if self.cur_input in self.sentences:
                self.times[self.sentences.index(self.cur_input)] += 1
                self.pair = self.preprocess(self.sentences, self.times)
            else:
                self.sentences.append(self.cur_input)
                self.times.append(1)
                self.pair = self.preprocess(self.sentences, self.times)
            
            self.preRoot = None
            self.cur_input = ""
            self.notaword = False
            return []
        if self.notaword:
            return []
        self.preRoot, returnList = self.trie.search_char(self.preRoot, c)
        if self.preRoot == None: # at the end of trie but isWord, after this search
                                 # must be all wrong for next input
            self.notaword = True
        if returnList == False:
            self.notaword = True
            return []
        ans = []
        returnSet = set(returnList)
        for p in self.pair:
            if p in returnSet:
                ans.append(p)
            if len(ans) >= 3:
                break
        return ans

    def preprocess(self, sentences, times):
        tmp = []
        for s, t in zip(sentences, times):
            self.trie.insert(s)    
            tmp.append([t, s])
        
        tmp.sort(reverse=True)
        tmp.append([-1,-1])
        pre_index, pre_i = -1, -1
        for index, (i, t) in enumerate(tmp):
            if pre_i != i:
                tmp[pre_index:index] = tmp[pre_index:index][::-1]
                pre_index = index
                pre_i = i
        return [x[1] for x in tmp[:-1]]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)






