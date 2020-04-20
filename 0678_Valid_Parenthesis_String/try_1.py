class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == '*':
                star.append(i)
            else:
                if left:
                    left.pop()
                else:
                    if star and star[0] < i:
                        del star[0]
                    else:
                        return False
        if left:
            for i in range(len(left)-1, -1, -1):
                if star and left[i] < star[-1]:
                    star.pop()
                    left[i] = -1
                else:                        
                    return False
        return True
