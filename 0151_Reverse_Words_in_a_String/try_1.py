class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        
        cur = ''
        for _s in s:
            if _s == ' ':
                if cur:
                    ans = cur + ' ' + ans
                cur = ''
            else:
                cur += _s
        
        if cur:
            ans = cur + ' ' + ans
        return ans[:-1]
