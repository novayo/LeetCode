# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def guess(a, b):
            return sum([_a == _b for _a, _b in zip(a, b)])
        
        target = random.choice(wordlist)
        ret = master.guess(target)
        while ret < 6:
            tmp = []
            for i in range(len(wordlist)):
                if guess(target, wordlist[i]) == ret:
                    tmp.append(wordlist[i])
            wordlist = tmp
            target = random.choice(wordlist)
            ret = master.guess(target)

