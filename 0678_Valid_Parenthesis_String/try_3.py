class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = collections.deque()
        
        for i, _s in enumerate(s):
            if _s == '(':
                left.append(i)
            elif _s == '*':
                star.append(i)
            else:
                if left:
                    left.pop()
                else:
                    # ) 只能用左邊的*
                    if star and star[0] < i:
                        star.popleft()
                    else:
                        return False
        # ( 只能用右邊的*
        if left:
            for i in range(len(left)-1, -1, -1):
                if star and star[-1] > left[i]:
                    star.pop()
                else:
                    return False
        return True