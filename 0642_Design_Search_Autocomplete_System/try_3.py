class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.cur_string = ''
        self.avaliable = []
        self.counter = collections.Counter()
        for s, t in zip(sentences, times):
            self.counter[s] += t
            
    def input(self, c: str) -> List[str]:
        if c == '#':
            self.counter[self.cur_string] += 1
            self.cur_string = ''
            self.avaliable = []
            return []
        
        if not self.cur_string:
            for s, t in self.counter.items():
                if s[0] == c:
                    self.avaliable.append((t, s))
            self.avaliable.sort(key=lambda x: (-x[0], x[1]))
            self.avaliable = [v[1] for v in self.avaliable]
        else:
            tmp_list = []
            for tmp in self.avaliable:
                if len(self.cur_string) < len(tmp) and tmp[len(self.cur_string)] == c:
                    tmp_list.append(tmp)
            self.avaliable = tmp_list
                
        self.cur_string += c
        return self.avaliable[:3]
        

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
