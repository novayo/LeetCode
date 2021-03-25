class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
	'''
	若[dog, dig] => dog => False，因為相同的d1g但有兩個不同的字
	若[dog, dog] => dog => True ，因為相同的d1g只有一個字且符合dog
	若[dog, dig] => cat => True ，因為沒有c1t
	'''
        self.abbre_set = collections.defaultdict(int)
        self.words = set()
        
        for word in dictionary:
            if word in self.words:
                continue
            self.abbre_set[self.getAbbreviation(word)] += 1
            self.words.add(word)

            
    def isUnique(self, word: str) -> bool:
        if self.abbre_set[self.getAbbreviation(word)] == 0:
            return True
        elif self.abbre_set[self.getAbbreviation(word)] == 1:
            if word in self.words:
                return True
            else:
                return False
        else:
            return False
            
    
    def getAbbreviation(self, word):
        if len(word) < 3:
            return word
        else:
            return word[0] + str(len(word)-2) + word[-1]

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)