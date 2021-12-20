class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dp = {}
        table = collections.defaultdict(list)
        
        for i in range(len(s)):
            table[s[i]].append(i)
        
        ans = 0
        for word in words:
            
            if dp.get(word, False):
                ans += 1
            else:
                index = -1
                for w in word:
                    if w not in table:
                        dp[word] = False
                        break

                    _i = bisect.bisect_right(table[w], index)
                    
                    if _i >= len(table[w]):
                        dp[word] = False
                        break
                    
                    index = table[w][_i]
                
                if dp.get(word, True):
                    dp[word] = True
                    ans += 1
        
        return ans
        
