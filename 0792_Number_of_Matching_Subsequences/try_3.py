class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        '''
        brute force: 5000 * 5000
        '''
        ans = 0
        is_answer = set()
        is_not_answer = set()
        start_index = {}
        
        for word in words:
            if word in is_not_answer:
                continue
            if word in is_answer:
                ans += 1
                continue
            
            # find start index
            i = j = 0
            for k in range(1, len(word)+1):
                if word[:k] in start_index:
                    j = start_index[word[:k]] + 1
                    i = k
                else:
                    break
            
            if i >= len(word):
                is_answer.add(word)
                ans += 1
                continue
            
            for j in range(j, len(s)):
                if word[i] == s[j]:
                    i += 1
                    start_index[word[:i]] = j
                    if i >= len(word):
                        is_answer.add(word)
                        ans += 1
                        break
            if i < len(word):
                is_not_answer.add(word)
        return ans
        
