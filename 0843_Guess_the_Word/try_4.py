# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        match = 0
        while match < len(wordlist[0]):
            guess = random.choice(wordlist)
            match = master.guess(guess)
            
            if match == len(wordlist[0]):
                break
            
            tmp = []
            for word in wordlist:
                cur_match = 0
                for i in range(len(guess)):
                    if guess[i] == word[i]:
                        cur_match += 1
                        if cur_match > match:
                            break
                
                if cur_match == match:
                    tmp.append(word)
            
            wordlist = tmp
        

