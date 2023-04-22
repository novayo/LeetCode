class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                return

            grid[i][j] = '0'

            dfs(grid, i-1, j)
            dfs(grid, i, j-1)
            dfs(grid, i+1, j)
            dfs(grid, i, j+1)

        def bfs(grid, i, j):
            queue = collections.deque()
            queue.append((i, j))

            while queue:
                x, y = queue.popleft()

                if grid[x][y] == '0':
                    continue
                grid[x][y] = '0'

                for i, j in [x-1, y], [x+1, y], [x, y+1], [x, y-1]:
                    if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                        continue
                    queue.append((i, j))

        def bfs_level_order(grid, i, j):
            queue = collections.deque()
            queue.append((i, j))

            while queue:
                next_layer = collections.deque()

                for x, y in queue:
                    if grid[x][y] == '0':
                        continue
                    grid[x][y] = '0'

                    for i, j in [x-1, y], [x+1, y], [x, y+1], [x, y-1]:
                        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                            continue
                        next_layer.append((i, j))

                queue = next_layer

        def bfs_set(grid, i, j):
            queue = set()
            queue.add((i, j))

            while queue:
                x, y = queue.pop()
                if grid[x][y] == '0':
                    continue
                grid[x][y] = '0'

                for i, j in [x-1, y], [x+1, y], [x, y+1], [x, y-1]:
                    if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                        continue
                    queue.add((i, j))

        def bfs_list(grid, i, j):
            queue = []
            queue.append((i, j))

            while queue:
                x, y = queue.pop()
                if grid[x][y] == '0':
                    continue
                grid[x][y] = '0'

                for i, j in [x-1, y], [x+1, y], [x, y+1], [x, y-1]:
                    if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
                        continue
                    queue.append((i, j))

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # dfs(grid, i, j)
                    # bfs(grid, i, j)
                    # bfs_level_order(grid, i, j)
                    # bfs_set(grid, i, j)
                    bfs_list(grid, i, j)
                    ans += 1
        return ans
