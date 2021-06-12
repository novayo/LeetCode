# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        '''
        選出相關度最高的去猜，去除random機制
        O(n^2)
        '''
        def match(word1, word2):
            count = 0
            for i in range(6):
                count += word1[i] == word2[i]
            return count
        
        # 算出相關程度 O(n^2)
        counter = collections.defaultdict(int)
        for word1 in wordlist:
            for word2 in wordlist:
                counter[word1] += match(word1, word2)

        for i in range(10):
            # 取得 最高相關
            _max, _max_word = 0, ''
            for word in wordlist:
                if _max < counter[word]:
                    _max = counter[word]
                    _max_word = word
            
            # 猜答案
            ret = master.guess(_max_word)
            if ret == 6:
                break
            
            # 更新wordlist
            wordlist2 = []
            for word in wordlist:
                if match(word, _max_word) == ret:
                    wordlist2.append(word)
            wordlist = wordlist2.copy()
