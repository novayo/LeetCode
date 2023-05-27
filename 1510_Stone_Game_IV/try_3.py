class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @functools.lru_cache(None)
        def isP1Win(player, n):
            if n <= 0:
                return not player
            
            if player:
                for i in range(1, int(sqrt(n)) + 1):
                    _pow = i**2
                    if isP1Win(False, n-_pow):
                        return True
                return False
            else:
                for i in range(1, int(sqrt(n)) + 1):
                    _pow = i**2
                    if not isP1Win(True, n-_pow):
                        return False
                return True
        
        return isP1Win(True, n)
