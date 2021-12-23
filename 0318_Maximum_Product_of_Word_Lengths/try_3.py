class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        words_set = set(words)
        
        while words_set:
            word = words_set.pop()
            
            _set = words_set.copy()
            while _set:
                word2 = _set.pop()
                
                if len(set(word) & set(word2)) == 0:
                    ans = max(ans, len(word)*len(word2))
        
        return ans