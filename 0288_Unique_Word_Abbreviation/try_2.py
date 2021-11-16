class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.origin = set()
        self.abbrev = {}
        
        for d in dictionary:
            
            if d in self.origin:
                continue
            
            self.origin.add(d)
            if len(d) <= 2:
                self.abbrev[d] = self.abbrev.get(d, 0) + 1
            else:
                a = d[0] + str(len(d)-2) + d[-1]
                self.abbrev[a] = self.abbrev.get(a, 0) + 1

    def isUnique(self, word: str) -> bool:
        a = word
        if len(word) <= 2:
            a = word
        else:
            a = word[0] + str(len(word)-2) + word[-1]
            
        if word in self.origin and self.abbrev[a] == 1:
            return True
        elif self.abbrev.get(a, 0) == 0:
            return True
        else:
            return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
