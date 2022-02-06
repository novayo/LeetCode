class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = left_bracket = 0
        
        for _s in s:
            if _s == '(':
                left_bracket += 1
            else:
                if left_bracket == 0:
                    ans += 1
                else:
                    left_bracket -= 1
        
        return ans + left_bracket
                
