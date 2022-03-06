class CombinationIterator:
    
    def __init__(self, characters: str, combinationLength: int):
        self.all_combs = self.getCombs(characters, combinationLength)
        self.index = 0
        
    def getCombs(self, characters, k):
        ans = []
        
        def recr(index, cur_list):
            nonlocal ans
            if len(cur_list) >= k:
                ans.append(''.join(cur_list))
                return
            
            for i in range(index, len(characters)):
                recr(i+1, cur_list + [characters[i]])
        
        recr(0, [])
        return ans
        
    def next(self) -> str:
        self.index += 1
        return self.all_combs[self.index-1]
        
    def hasNext(self) -> bool:
        return self.index < len(self.all_combs)


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
