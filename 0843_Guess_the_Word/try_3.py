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
        Optimize: 算字母在每個位置的出現次數當作是相關程度 => O(n)
        '''
        def match(word1, word2):
            count = 0
            for i in range(6):
                count += word1[i] == word2[i]
            return count
        
        # 算出相關程度 O(n)
        counter = collections.defaultdict(lambda: collections.defaultdict(int))
        for word1 in wordlist:
            for i in range(len(word1)):
                counter[i][word1[i]] += 1

        for i in range(10):
            # 計算總分, 並取出最高相關(最高分數)
            _max, _max_word = 0, ''
            for word in wordlist:
                score = 0
                for i in range(len(word)):
                    score += counter[i][word[i]]
                
                if _max < score:
                    _max = score
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
