class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (len(x), x))
        
        ans = ''
        cache = set()
        for word in words:
            if len(word) == 1:
                if len(word) > len(ans):
                    ans = word
                cache.add(word)
            elif word[:-1] in cache:
                if len(word) > len(ans):
                    ans = word
                cache.add(word)
        return ans
