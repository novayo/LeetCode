class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        height = len(heightMap)
        width = len(heightMap[0])
        
        cache = set()
        pq = []
        for i in range(height):
            for j in range(width):
                if i == 0 or j == 0 or i == height-1 or j == width-1:
                    cache.add((i, j))
                    heapq.heappush(pq, (heightMap[i][j], i, j))
        
        ans = 0
        while pq:
            h, i, j = heapq.heappop(pq)
            
            for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                if not (0 <= x < height and 0 <= y < width) or (x, y) in cache:
                    continue
                
                ans += max(0, h - heightMap[x][y])
                heapq.heappush(pq, (max(h, heightMap[x][y]), x, y))
                cache.add((x, y))
        
        return ans    
