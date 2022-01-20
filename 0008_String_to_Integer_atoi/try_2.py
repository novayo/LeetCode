class Solution:
    def myAtoi(self, s: str) -> int:    
        s = s.strip()
        if len(s) == 0:
            return 0
        
        ans = 0
        isneg = False
        if s[0] == '-':
            if len(s) > 1 and s[1].isdigit():
                isneg = True
                ans = int(s[1])
                s = s[2:]
            else:
                return 0
        elif s[0] == '+':
            if len(s) > 1 and s[1].isdigit():
                ans = int(s[1])
                s = s[2:]
            else:
                return 0
        elif not s[0].isdigit():
            return 0
        
        for i in range(len(s)):
            if not s[i].isdigit():
                break
            ans *= 10
            ans += int(s[i])
        
        if isneg:
            ans *= -1
        
        if ans < -2**31:
            ans = -2**31
        elif ans > 2**31-1:
            ans = 2**31-1
        return ans
