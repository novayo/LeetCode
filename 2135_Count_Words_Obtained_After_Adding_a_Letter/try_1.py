class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        # O(n+m+26n) time / O(n)
        def convert2bit(word):
            ret = 0
            for w in word:
                ret |= (1 << (ord(w)-ord('a')))
            return ret
        
        # init
        startSet = set()
        for word in startWords:
            startSet.add(convert2bit(word))
        
        # loop
        ans = 0
        for word in targetWords:
            bit = convert2bit(word)
            
            for w in word:
                if bit ^ (1 << (ord(w)-ord('a'))) in startSet:
                    ans += 1
                    break
        return ans
