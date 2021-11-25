class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        '''
        將words計算完數量之後，sort => 每次query計算完的時候，做binary search right => 答案為len - index
        
        計算 => 記得當前最小，並記錄個數，遇到最小的就更新
        '''
        
        def calculate(word):
            c, i = None, 0
            
            for w in word:
                if not c:
                    c = w
                    i = 1
                elif w < c:
                    c = w
                    i = 1
                elif w == c:
                    i += 1
            
            return i
        
        for i in range(len(words)):
            words[i] = calculate(words[i])
        
        words.sort()
        
        # get ans
        ans = []
        for query in queries:
            index = bisect.bisect_right(words, calculate(query))
            ans.append(len(words) - index)
        
        return ans
