class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        def find(w1, w2):
            ret = float('inf')
            i = j = 0
            while j < n:
                while j < n and wordsDict[j] != w1:
                    j += 1

                if j >= n:
                    break

                i = j+1
                while i < n and wordsDict[i] != w2:
                    if wordsDict[i] == w1:
                        j = i
                    i += 1

                if i >= n:
                    break

                ret = min(ret, i-j)
                j = i
            return ret
        
        n = len(wordsDict)
        return min(find(word1, word2), find(word2, word1))
