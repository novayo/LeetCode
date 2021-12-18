class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        '''
        sorted length
        [a, c1, c2, c3, c4, a1, a_3, a_4, a2]
         1                   2。  3    4   3
        '''
        
        def same(w1, w2):
            for i in range(len(w2)):
                target = w2[:i] + w2[i+1:]
                if target == w1:
                    return True
            return False
        
        length_mapping = collections.defaultdict(set)
        word_mapping = {}
        
        min_length, max_length = float('inf'), -float('inf')
        for word in words:
            length_mapping[len(word)].add(word)
            word_mapping[word] = 1
            
            min_length = min(min_length, len(word))
            max_length = max(max_length, len(word))
        
        ans = 1
        for length in range(min_length+1, max_length+1):
            
            for word in length_mapping[length]:
                for pre_word in length_mapping[length-1]:
                    if same(pre_word, word):
                        word_mapping[word] = max(word_mapping[word], word_mapping[pre_word]+1)
                        ans = max(ans, word_mapping[word])
        
        return ans
                    
                    
