class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        height, width = len(mat), len(mat[0])
        
        # get table
        table = {}
        current = 0
        offset = 0
        for i in range(height):
            for j in range(width):
                table[i, j] = 1 << offset
                
                if mat[i][j] == 1:
                    current += 1 << offset
                
                offset += 1
        
        # bfs
        cache = set([current])
        que = [current]
        step = 0
        
        while que:
            next_que = []
            for matrix in que:
                if matrix == 0:
                    return step
                
                # flip all cells
                for i in range(height):
                    for j in range(width):
                        tmp = matrix
                        for x, y in [i, j], [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                            if not (0 <= x < height and 0 <= y < width):
                                continue
                            tmp ^= table[x, y]
                        
                        if tmp not in cache:
                            cache.add(tmp)
                            next_que.append(tmp)
            que = next_que
            step += 1
        
        return -1
                            
            
