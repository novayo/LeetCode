class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        1. 比較兩word最少有幾個不同 => 找出最長的已經有的sub word，答案為len(word1) - 最長長度
           => 不能從尾巴來，因為可能是中間最長，其他兩邊打掉 => 查詢為n^3
        2. 硬爆所有可能
        '''
        
        def recr(word1, word2, memo={}):
            
            if not word1 and not word2:
                return 0
            
            if not word1 and word2:
                memo[(word1, word2)] = len(word2)
                return memo[(word1, word2)]
            
            if word1 and not word2:
                memo[(word1, word2)] = len(word1)
                return memo[(word1, word2)]
            
            if word1[0] == word2[0]:
                memo[(word1, word2)] = recr(word1[1:], word2[1:], memo)
                return memo[(word1, word2)]
            
            # replace, delete, insert
            memo[(word1, word2)] = min(recr(word1[1:], word2[1:], memo), recr(word1[1:], word2, memo), recr(word1, word2[1:], memo)) + 1
            return memo[(word1, word2)]
        
        
        return recr(word1, word2)
