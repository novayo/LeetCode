class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.time = 0

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Node()
        self.cur_root = self.root
        self.cur_string = ''

        for sentence, t in zip(sentences, times):
            self.add(sentence, t)
    
    def add(self, sentence, time):
        root = self.root
        for s in sentence:
            root = root.children[s]
        root.time += time
    
    def queryTop3(self, root, string):
        if root.time != 0:
            ret = [(root.time, string)]
        else:
            ret = []
            
        for char, next_root in root.children.items():
            ret += self.queryTop3(next_root, string+char)
            ret.sort(key=lambda x: (-x[0], x[1]))
            ret = ret[:3]
        return ret
        
        
    def input(self, c: str) -> List[str]:
        if c == '#':
            self.add(self.cur_string, 1)
            self.cur_string = ''
            self.cur_root = self.root
            return []
        
        self.cur_string += c
        self.cur_root = self.cur_root.children[c]
        ret = self.queryTop3(self.cur_root, self.cur_string)
        return [v[1] for v in ret]
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
