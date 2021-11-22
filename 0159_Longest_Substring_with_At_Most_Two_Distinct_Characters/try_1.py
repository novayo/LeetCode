class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        '''
        Two pointer
        
        #p1: i 應該要記得 最後一個不同的位置
            EX: eeecceee => i = 5
        '''
        
        i = l = r = 0
        last = None
        found = set()
        
        ans = 0
        while r < len(s):
            found.add(s[r])
            
            if len(found) > 2:
                ans = max(ans, r-l)
                found = set([s[r], last])
                l = i
            
            #p1
            if not last:
                last = s[r]
            elif last != s[r]:
                i = r
                last = s[i]
            
            r += 1
        
        ans = max(ans, r-l)
        return ans
                
