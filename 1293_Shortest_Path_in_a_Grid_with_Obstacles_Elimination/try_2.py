class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # (steps, i, j, k)
        # 走過的位置：不用再走一次，如果之前到這裡的k比較多的話
        height, width = len(grid), len(grid[0])
        cache = {}
        pq = [(0, 0, 0, k)]
        
        while pq:
            step, i, j, _k = heapq.heappop(pq)
            
            if i == height-1 and j == width-1:
                return step
            
            for _i, _j in [i-1,j], [i+1,j], [i,j-1], [i,j+1]:
                if not (0 <= _i < height and 0 <= _j < width):
                    continue
                
                # 如果不能再破壞牆壁了
                if grid[_i][_j] == 1 and _k == 0:
                    continue
                
                # 如果之前走過，且之前的_k比較多 => 不用再走一次
                if cache.get((_i, _j), -1) >= _k:
                    continue
                
                # 走
                if grid[_i][_j] == 1:
                    cache[_i, _j] = _k-1
                    heapq.heappush(pq, (step+1, _i, _j, _k-1))
                else:
                    cache[_i, _j] = _k
                    heapq.heappush(pq, (step+1, _i, _j, _k))
        
        return -1

