class StreamChecker:

    def __init__(self, words: List[str]):
        self.word_set = set(words)
        self.cur_search = ""
    
    def query(self, letter: str) -> bool:
        self.cur_search += letter
        if len(self.cur_search) > 200:
            self.cur_search = self.cur_search[1:]

        for i in range(1, len(self.cur_search)+1):
            if self.cur_search[-i:] in self.word_set:
                return True
            
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
