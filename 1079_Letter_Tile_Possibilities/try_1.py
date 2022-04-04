class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        
        def recr(i):
            if i >= n:
                return set()
            
            ret = recr(i+1)
            for tile in ret.copy():
                if len(tile) >= n:
                    continue
                for j in range(len(tile)+1):
                    ret.add(tile[:j] + tiles[i] + tile[j:])
            ret.add(tiles[i])
            return ret
        
        return len(recr(0))
