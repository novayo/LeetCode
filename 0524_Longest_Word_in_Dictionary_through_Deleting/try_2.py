class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        self._dict = collections.defaultdict(list)
        
        for i, v in enumerate(s):
            self._dict[v].append(i)
            
        ans = ""
        for v in sorted(d):
            if self.is_sub(v):
                ans = max(ans, v, key=len)
        return ans
    
    def is_sub(self, word):
        pre = -1
        for w in word:
            if w not in self._dict:
                return False
            index = bisect.bisect_right(self._dict[w], pre)
            if index == len(self._dict[w]):
                return False
            pre = self._dict[w][index]
        return True
