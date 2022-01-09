class MagicDictionary:

    def __init__(self):
        self.collection = collections.defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:
        for string in dictionary:
            for i in range(len(string)):
                mask = string[:i]+'#'+string[i+1:]
                self.collection[mask].add(string)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            mask = searchWord[:i] + '#' + searchWord[i+1:]
            if mask in self.collection \
               and (len(self.collection[mask]) > 1 or searchWord not in self.collection[mask]):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
