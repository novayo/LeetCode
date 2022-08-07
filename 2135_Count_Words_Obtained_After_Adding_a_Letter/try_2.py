class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        cache = set()
        
        for start in startWords:
            bit = 0
            for s in start:
                bit += (1 << (ord(s) - ord('a')))
            
            for i in range(26):
                if bit & (1 << i) > 0:
                    continue
                
                cache.add(bit + (1<<i))
        
        ans = 0
        for target in targetWords:
            bit = 0
            for s in target:
                bit += (1 << (ord(s) - ord('a')))
            
            if bit in cache:
                ans += 1
        return ans
