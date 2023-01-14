class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        '''
        TC: O(9 * 10**6)
        SC: O(10**5)
        '''
        # 1. Get word_set: O(len(words)) = O(10**4)
        word_set = set()
        for word in words:
            word_set.add(word)
        
        # 2. recursion: O(len(word)**2) = O(900)
        def helper(s_index, word):
            if s_index >= len(word):
                return True
            
            for j in range(s_index+1, len(word)+1):
                if s_index == 0 and j == len(word):
                    break
                
                if word[s_index:j] in word_set:
                    if helper(j, word):
                        return True
            return False
        
        # 3. get answer: O(len(words) * O(helper)) = O(9*10**6)
        ans = []
        for word in words:
            if helper(0, word):
                ans.append(word)
        return ans

