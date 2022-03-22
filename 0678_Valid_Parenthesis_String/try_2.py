class Solution:
    def checkValidString(self, s: str) -> bool:
        
        memo = set()
        def recr(i, score):
            if i >= len(s):
                return score == 0
            
            if score < 0:
                return False
            
            _s = s[i]
            
            if (i, score) in memo:
                return False
            
            ret = False
            if _s == '(':
                ret = ret or recr(i+1, score+1)
            elif _s == ')':
                ret = ret or recr(i+1, score-1)
            else:
                ret = ret or recr(i+1, score) or recr(i+1, score+1) or recr(i+1, score-1)
            
            memo.add((i, score))
            return ret
        
        return recr(0, 0)
            