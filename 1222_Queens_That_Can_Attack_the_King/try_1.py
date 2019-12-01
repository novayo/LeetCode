class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = collections.deque()
        
        # up
        tmpy = king[1]
        while tmpy>=0:
            tmpy -= 1
            if [king[0], tmpy] in queens:
                ans.append([king[0], tmpy])
                break
        # top right
        tmpx, tmpy = king[0], king[1]
        while tmpx<8 and tmpy>=0:
            tmpx+=1
            tmpy-=1
            if [tmpx, tmpy] in queens:
                ans.append([tmpx, tmpy])
                break
        # right
        tmpx = king[0]
        while tmpx<8:
            tmpx += 1
            if [tmpx,king[1]] in queens:
                ans.append([tmpx, king[1]])
                break
        # down right
        tmpx, tmpy = king[0], king[1]
        while tmpx<8 and tmpy<8:
            tmpx+=1
            tmpy+=1
            if [tmpx, tmpy] in queens:
                ans.append([tmpx, tmpy])
                break
        # down
        tmpy = king[1]
        while tmpy<8:
            tmpy += 1
            if [king[0],tmpy] in queens:
                ans.append([king[0], tmpy])
                break
        # down left
        tmpx, tmpy = king[0], king[1]
        while tmpx>=0 and tmpy<8:
            tmpx-=1
            tmpy+=1
            if [tmpx, tmpy] in queens:
                ans.append([tmpx, tmpy])
                break
        # left
        tmpx = king[0]
        while tmpx>=0:
            tmpx -= 1
            if [tmpx,king[1]] in queens:
                ans.append([tmpx, king[1]])
                break
        # top left
        tmpx, tmpy = king[0], king[1]
        while tmpx>=0 and tmpy>=0:
            tmpx-=1
            tmpy-=1
            if [tmpx, tmpy] in queens:
                ans.append([tmpx, tmpy])
                break
        return sorted(ans)
