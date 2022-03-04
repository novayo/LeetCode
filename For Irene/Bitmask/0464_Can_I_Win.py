class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal == 0:
            return True
        
        memo = {}
        def minmax(total, p1_turn=True, bitmask=0):
            if total >= desiredTotal:
                memo[bitmask] = not p1_turn
                return memo[bitmask] 
            
            if bitmask == 2**maxChoosableInteger-1:
                memo[bitmask] = False
                return memo[bitmask]
            
            if bitmask not in memo:
                if p1_turn:
                    ret = False
                    for i in range(1, maxChoosableInteger+1):
                        if bitmask & (1<<i-1) != 0:
                            continue

                        ret = ret or minmax(total+i, not p1_turn, bitmask | (1<<i-1))
                        if ret:
                            break
                    memo[bitmask] = ret
                else:
                    ret = True
                    for i in range(1, maxChoosableInteger+1):
                        if bitmask & (1<<i-1) != 0:
                            continue

                        ret = ret and minmax(total+i, not p1_turn, bitmask | (1<<i-1))
                        if ret == False:
                            break
                    memo[bitmask] = ret
            return memo[bitmask]
        
        return minmax(0)
        
