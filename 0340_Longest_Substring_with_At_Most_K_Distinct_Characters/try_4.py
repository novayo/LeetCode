class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        od = collections.OrderedDict()
        
        ans = i = 0
        for j, _s in enumerate(s):
            if _s in od:
                od.move_to_end(_s)
            
            od[_s] = j
            
            if len(od) > k:
                i = od.popitem(last=False)[1] + 1 # (key, value)
            
            ans = max(ans, j-i+1)
        
        return ans