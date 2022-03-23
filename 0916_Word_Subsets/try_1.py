class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        condition = collections.Counter()
        
        for word in words2:
            for c, v in collections.Counter(word).items():
                condition[c] = max(condition[c], v)
        
        ans = []
        for word in words1:
            counter = collections.Counter(word)
            
            isMatch = True
            for c, v in condition.items():
                if counter[c] < v:
                    isMatch = False
                    break
            if isMatch:
                ans.append(word)
        return ans