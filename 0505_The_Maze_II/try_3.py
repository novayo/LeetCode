class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        pq = [(0, start[0], start[1])] # (距離, x, y)
        cache = {(start[0], start[1]): 0}

        while pq:
            dist, x, y = heapq.heappop(pq)

            if [x, y] == destination:
                return dist
            
            # go up
            d, i, j = dist, x, y
            while i > 0 and maze[i-1][j] == 0:
                d += 1
                i -= 1
            
            if (i, j) not in cache or d < cache[i, j]:
                cache[i, j] = d
                heapq.heappush(pq, (d, i, j))
            
            # go down
            d, i, j = dist, x, y
            while i < len(maze) - 1 and maze[i+1][j] == 0:
                d += 1
                i += 1

            if (i, j) not in cache or d < cache[i, j]:
                cache[i, j] = d
                heapq.heappush(pq, (d, i, j))
            
            # go left
            d, i, j = dist, x, y
            while j > 0 and maze[i][j-1] == 0:
                d += 1
                j -= 1

            if (i, j) not in cache or d < cache[i, j]:
                cache[i, j] = d
                heapq.heappush(pq, (d, i, j))

            # go right
            d, i, j = dist, x, y
            while j < len(maze[0]) - 1 and maze[i][j+1] == 0:
                d += 1
                j += 1

            if (i, j) not in cache or d < cache[i, j]:
                cache[i, j] = d
                heapq.heappush(pq, (d, i, j))
        
        return -1
