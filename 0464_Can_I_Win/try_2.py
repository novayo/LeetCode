class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @functools.lru_cache(None)
        def isPlayer1Win(player, bitmask, number):
            if number >= desiredTotal:
                return not player
            
            if bitmask == 2**maxChoosableInteger-1:
                return False
            
            if player:
                for i in range(1, maxChoosableInteger+1):
                    if bitmask & (1 << (i-1)) != 0:
                        continue
                    if isPlayer1Win(False, bitmask | (1 << (i-1)), number + i):
                        return True
                return False
            else:
                for i in range(1, maxChoosableInteger+1):
                    if bitmask & (1 << (i-1)) != 0:
                        continue
                    if not isPlayer1Win(True, bitmask | (1 << (i-1)), number + i):
                        return False
                return True
        
        if desiredTotal == 0:
            return True
        return isPlayer1Win(True, 0, 0)
