class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        ans = 0
        counter = collections.Counter()
        words.sort(key=len)
        
        for word in words:
            for i in range(len(word)):
                t = word[:i] + word[i+1:]
                counter[word] = max(counter[word], counter[t]+1)
                ans = max(ans, counter[word])
        return ans
