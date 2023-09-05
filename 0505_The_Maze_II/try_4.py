class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        height, width = len(maze), len(maze[0])
        que = collections.deque()
        cache = {}

        # init
        que.append((0, start)) # dist, pos

        ans = float('inf')
        while que:
            dist, pos = que.popleft()

            if pos[0] == destination[0] and pos[1] == destination[1]:
                ans = min(ans, dist)
                continue
            
            # go up
            x, y = pos
            step = 0
            while x > 0 and maze[x-1][y] == 0:
                step += 1
                x -= 1
            if dist + step < cache.get((x, y), float('inf')):
                cache[x, y] = dist + step
                que.append((dist + step, (x, y)))
            
            # go right
            x, y = pos
            step = 0
            while y < width - 1 and maze[x][y+1] == 0:
                step += 1
                y += 1
            if dist + step < cache.get((x, y), float('inf')):
                cache[x, y] = dist + step
                que.append((dist + step, (x, y)))

            # go down
            x, y = pos
            step = 0
            while x < height - 1 and maze[x+1][y] == 0:
                step += 1
                x += 1
            if dist + step < cache.get((x, y), float('inf')):
                cache[x, y] = dist + step
                que.append((dist + step, (x, y)))
            
            # go left
            x, y = pos
            step = 0
            while y > 0 and maze[x][y-1] == 0:
                step += 1
                y -= 1
            if dist + step < cache.get((x, y), float('inf')):
                cache[x, y] = dist + step
                que.append((dist + step, (x, y)))

        return ans if ans < float('inf') else -1

