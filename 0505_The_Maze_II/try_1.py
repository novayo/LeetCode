class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        height = len(maze)
        width = len(maze[0])
        
        priority_queue = [(0, start[0], start[1])]
        
        found = {}
        found[start[0], start[1]] = 0
        
        ans = float('inf')
        while priority_queue:
            dist, x, y = heapq.heappop(priority_queue)
        
            if dist >= ans:
                break
        
            if [x, y] == destination:
                if dist < ans:
                    ans = dist
                continue
        
            # up
            i, j = x, y
            while i >= 0 and maze[i][j] == 0:
                i -= 1
            i += 1
            if found.get((i, j), float('inf')) > dist + x-i:
                heapq.heappush(priority_queue, (dist + x-i, i, j))
                found[i, j] = dist + x-i
            
            # right
            i, j = x, y
            while j < width and maze[i][j] == 0:
                j += 1
            j -= 1
            if found.get((i, j), float('inf')) > dist + j-y:
                heapq.heappush(priority_queue, (dist + j-y, i, j))
                found[i, j] = dist + j-y
            
            # down
            i, j = x, y
            while i < height and maze[i][j] == 0:
                i += 1
            i -= 1
            if found.get((i, j), float('inf')) > dist + i-x:
                heapq.heappush(priority_queue, (dist + i-x, i, j))
                found[i, j] = dist + i-x
            
            # left
            i, j = x, y
            while j >= 0 and maze[i][j] == 0:
                j -= 1
            j += 1
            if found.get((i, j), float('inf')) > dist + y-j:
                heapq.heappush(priority_queue, (dist + y-j, i, j))
                found[i, j] = dist + y-j
        
        return ans if ans != float('inf') else -1
