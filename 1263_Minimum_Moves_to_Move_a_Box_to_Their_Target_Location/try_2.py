class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        '''
        N = 400 ^ 2

        1. S 是否能到 B
        2.  可以
            算B => T的距離
        '''
        height, width = len(grid), len(grid[0])

        def is_s_to_b(i1,j1,i2,j2,b_i,b_j):
            if grid[i2][j2] == "#":
                return False
            que = [(i1,j1)]
            done_set = set()
            done_set.add((i1, j1))

            while que:
                que2 = []
                for i, j in que:
                    if i == i2 and j == j2:
                        return True
                    
                    for x,y in [i-1,j],[i+1,j],[i,j-1],[i,j+1]:
                        if not (0 <= x < height and 0 <= y < width):
                            continue
                        if grid[x][y] == "#" or (x==b_i and y==b_j) or (x,y) in done_set:
                            continue
                        que2.append((x, y))
                        done_set.add((x, y))
                
                que = que2
            return False

        pos_t, pos_b, pos_s = [], [], []
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "T":
                    pos_t = [i, j]
                elif grid[i][j] == "B":
                    pos_b = [i, j]
                elif grid[i][j] == "S":
                    pos_s = [i, j]
        
        que = [(pos_b[0], pos_b[1], pos_s[0], pos_s[1])]
        step = 0
        done_set = set()
        done_set.add((pos_b[0], pos_b[1], pos_s[0], pos_s[1]))

        while que:
            que2 = []
            for i, j, s_i, s_j in que:
                if i == pos_t[0] and j == pos_t[1]:
                    return step
                
                for x, y, s_x, s_y in [i-1,j,i+1,j],[i+1,j,i-1,j],[i,j-1,i,j+1],[i,j+1,i,j-1]:
                    if not (0 <= x < height and 0 <= y < width and 0 <= s_x < height and 0 <= s_y < width):
                        continue
                    
                    if grid[x][y] == "#":
                        continue

                    if (x, y, i, j) in done_set:
                        continue

                    if not is_s_to_b(s_i, s_j, s_x, s_y, i, j):
                        continue

                    que2.append((x, y, i, j))
                    done_set.add((x, y, i, j))
            
            step += 1
            que = que2

        return -1
