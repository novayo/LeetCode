class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        ptr = self.root
        for w in word:
            ptr = ptr.children[w]
        ptr.is_word = True
    
    # 回傳所有的字串
    def search(self, word):
        ptr = self.root
        for w in word:
            if w not in ptr.children:
                return []
            ptr = ptr.children[w]
        
        ans_list = []
        def recr(node, cur_string):
            if node.is_word:
                ans_list.append(cur_string)
            
            for w in node.children:
                recr(node.children[w], cur_string + w)
        
        recr(ptr, word)
        return ans_list


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self._input = ''
        self.history_table = collections.Counter()
        self.trie = Trie()
        
        for word, time in zip(sentences, times):
            self.history_table[word] = time
            self.trie.insert(word)

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.history_table[self._input] += 1
            self.trie.insert(self._input)
            self._input = ""
            return []
        else:
            self._input += c
        
        prefix_string_list = self.trie.search(self._input)
        _ans_list = sorted([(-self.history_table[string], string) for string in prefix_string_list])[:3]
        return [v[1] for v in _ans_list]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

