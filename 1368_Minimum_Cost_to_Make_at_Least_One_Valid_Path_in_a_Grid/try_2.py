class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        '''
        每一次挑cost最小 & (目前離終點的直線距離最小 => 自己實踐heap去比較)
            => 每個點都可以，要換or不換
        
        但可能會走到重複的點 => 用dict存起來，若cost比較小，才能放進去heap (每次取出來之前也去比較一次)
        '''
        def getPos(x, y, move):
            if move == 1:
                y += 1
            elif move == 2:
                y -= 1
            elif move == 3:
                x += 1
            else:
                x -= 1
            return x, y
        
        def heuristic(i, j, cost):
            return cost*0.1 + i + j
        
        height = len(grid)
        width = len(grid[0])
        table = collections.defaultdict(lambda: float('inf'))
        heap = [(heuristic(0, 0, 0), 0, 0, 0)]
        
        while heap:
            h, cost, i, j = heapq.heappop(heap)
            
            if i == height-1 and j == width-1:
                return cost
            
            # 拿出來之後先比較一次
            if h >= table[i, j]:
                continue
            else:
                table[i, j] = h
            
            for move in range(1, 5):
                x, y = getPos(i, j, move)
                if 0 <= x < height and 0 <= y < width and table[x, y] > heuristic(cost, x, y):
                    
                    if move == grid[i][j]:
                        heapq.heappush(heap, (heuristic(cost, x, y), cost, x, y))
                    else:
                        heapq.heappush(heap, (heuristic(cost+1, x, y), cost+1, x, y))
        
        return -1