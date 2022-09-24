class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_dict = collections.Counter()
        
        for word in words:
            for i in range(1, len(word)+1):
                prefix_dict[word[:i]] += 1
        
        ans = []
        for word in words:
            _sum = 0
            for i in range(1, len(word)+1):
                _sum += prefix_dict[word[:i]]
            ans.append(_sum)
        return ans
