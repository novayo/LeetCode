class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def getFreq(word):
            counter = collections.Counter(word)
            return counter[sorted(counter.keys())[0]]
        
        wordMaxLength = 10
        freqs = [0] * (wordMaxLength+1)
        
        # count
        for word in words:
            f = getFreq(word)
            freqs[f] += 1
        
        # presum
        for i in range(1, wordMaxLength+1):
            freqs[i] += freqs[i-1]
        
        # get answer
        ans = [0] * len(queries)
        for i, word in enumerate(queries):
            ans[i] = freqs[-1] - freqs[getFreq(word)]
        
        return ans
