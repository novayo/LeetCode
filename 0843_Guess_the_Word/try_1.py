# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        count = 0
        guess_max = 0
        while guess_max != 6:
            count += 1
            # 取得一個去猜
            target = random.choice(wordlist)
            number = master.guess(target)
            
            # 更新找到的答案
            guess_max = max(guess_max, number)
            if guess_max == 6:
                break
            
            # 用 target 跟其他人玩1A1B, 取出跟number一樣的字
            new_wordlist = []
            for word in wordlist:
                same_count = self.get_1A1B(target, word)
                if same_count == number:
                    new_wordlist.append(word)
            
            wordlist = new_wordlist
        
        print(count)
    
    def get_1A1B(self, target, other):
        same_count = 0
        for i in range(6):
            if target[i] == other[i]:
                same_count += 1
        return same_count

