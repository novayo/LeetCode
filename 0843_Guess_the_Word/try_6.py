# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def get_diff_number(s1, s2):
            return sum(s1[i] == s2[i] for i in range(len(s1)))
        
        cache = set()
        while True:
            idx = random.randint(0, len(wordlist)-1)
            while wordlist[idx] in cache:
                idx = random.randint(0, len(wordlist)-1)
            
            cache.add(wordlist[idx])
            
            target = master.guess(wordlist[idx])
            if target == 6:
                break
            
            tmp = []
            for i in range(len(wordlist)):
                if i == idx:
                    continue
                if get_diff_number(wordlist[idx], wordlist[i]) == target:
                    tmp.append(wordlist[i])
                
            wordlist = tmp
        