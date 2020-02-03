class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x < y:
            x, y = y, x
        
        if x == 1 and y == 0:
            return 3
        elif x == 2 and y == 2:
            return 4
        
        ans = 0
        while not(x == y or y == 0):
            ans += 1
            x -= 2
            y -= 1
        
        if x == y:
            if x > 3:
                ans += (4+2*((x-4)//3))
            elif x > 0:
                ans += 2
        else:
            if x > 1:
                ans += (2*((x-2)//4+1)+(((x-2)%4) & 1))
            elif x > 0:
                ans += 1
        return ans
