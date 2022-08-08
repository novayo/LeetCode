class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        height, width = len(maze), len(maze[0])
        cache = {(start[0], start[1]): 0}
        pq = [(0, start[0], start[1])] # (score, x, y)
        
        while pq:
            score, x, y = heapq.heappop(pq)
            
            if [x, y] == destination:
                return score
            
            # go up
            i, j = x, y
            while i > 0 and maze[i-1][j] == 0:
                i -= 1
            
            if cache.get((i, j), float('inf')) > score+x-i:
                heapq.heappush(pq, (score+x-i, i, j))
                cache[i, j] = score+x-i
            
            # go right
            i, j = x, y
            while j < width-1 and maze[i][j+1] == 0:
                j += 1
            
            if cache.get((i, j), float('inf')) > score+j-y:
                heapq.heappush(pq, (score+j-y, i, j))
                cache[i, j] = score+j-y
            
            # go down
            i, j = x, y
            while i < height-1 and maze[i+1][j] == 0:
                i += 1
                
            if cache.get((i, j), float('inf')) > score+i-x:
                heapq.heappush(pq, (score+i-x, i, j))
                cache[i, j] = score+i-x
            
            # go left
            i, j = x, y
            while j > 0 and maze[i][j-1] == 0:
                j -= 1
                
            if cache.get((i, j), float('inf')) > score+y-j:
                heapq.heappush(pq, (score+y-j, i, j))
                cache[i, j] = score+y-j
            
        return -1
'''
[
[0,b,1,0,a],
[0,0,0,0,0],
[0,0,0,1,0],
[1,1,0,1,1],
[0,0,0,0,0]]

[0,4]
[0,1]

'''
