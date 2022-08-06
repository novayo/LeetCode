class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.num = 2**(len(self.characters)) - 1

    def num_bit(self):
        return collections.Counter(bin(self.num)[2:])['1']
        
    def next(self) -> str:
        while self.num > 0 and self.num_bit() != self.combinationLength:
            self.num -= 1
        
        ret = ''
        for i in range(len(self.characters)):
            if self.num & (1 << (len(self.characters)-i-1)) > 0:
                ret += self.characters[i]
        
        self.num -= 1
        while self.num > 0 and self.num_bit() != self.combinationLength:
            self.num -= 1
            
        return ret

    def hasNext(self) -> bool:
        return self.num > 0

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()