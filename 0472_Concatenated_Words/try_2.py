class Trie:
    def __init__(self, words):
        self.root = {}
        
        for word in words:
            root = self.root
            for w in word:
                if w not in root:
                    root[w] = {'isWord': False}
                root = root[w]
            root['isWord'] = True
    
    # Recursion: O(len(word)**2) = O(900)
    def helper(self, word):
        def _helper(s_index):
            if s_index >= len(word):
                return True
            
            root = self.root
            for j in range(s_index, len(word)):
                if s_index == 0 and j == len(word)-1:
                    break
                
                w = word[j]
                if w not in root:
                    break
                
                if root[w]['isWord']:
                    if _helper(j+1):
                        return True
                root = root[w]
            return False
        return _helper(0)
        

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        '''
        TC: O(9 * 10**6)
        SC: O(10**5)
        '''
        # Get answer: O(len(words) * O(helper)) = O(9*10**6)
        trie = Trie(words)
        ans = []
        for word in words:
            if trie.helper(word):
                ans.append(word)
        return ans

