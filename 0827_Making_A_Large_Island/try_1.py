class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        group_map = {}
        pos_map = {}
        
        # for loop => if 1 => do bfs
        # return: score
        def bfs(i, j):
            found = set()
            queue = set()
            
            queue.add((i, j))
            while queue:
                x, y = queue.pop()
                
                found.add((x, y))
                grid[x][y] = 'x' # fix
                
                for _x, _y in [x-1, y], [x+1, y], [x, y-1], [x, y+1]:
                    if _x < 0 or _y < 0 or _x >= len(grid) or _y >= len(grid[0]) or grid[_x][_y] != 1:
                        continue
                    queue.add((_x, _y))
            
            return found
        
        # init
        ans = 0
        group = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_set = bfs(i, j)
                    cur_score = len(cur_set)
                    
                    ans = max(cur_score, ans)
                    
                    # group_map[group] = len(found)
                    group_map[group] = cur_score
        
                    # pop found => set all pos in found to pos_map[i, j] = len(found)
                    while cur_set:
                        x, y = cur_set.pop()
                        pos_map[x, y] = group
                    
                    group += 1
        
        # for loop => if 0 => get groups from group_map[four directions] => get score from group => get max answer
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    # get group
                    get_groups = set()
                    for _x, _y in [x-1, y], [x+1, y], [x, y-1], [x, y+1]:
                        if _x < 0 or _y < 0 or _x >= len(grid) or _y >= len(grid[0]) or grid[_x][_y] != 'x':
                            continue
                        get_groups.add(pos_map[_x, _y])
                    
                    # calculate sum
                    cur_sum = 1
                    while get_groups:
                        cur_sum += group_map[get_groups.pop()]
                    
                    ans = max(ans, cur_sum)
        
        return ans