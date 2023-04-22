class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def isValid(x, y):
            return 0 <= x < height and 0 <= y < width and maze[x][y] == 0

        height, width = len(maze), len(maze[0])
        found = set()
        queue = set()

        queue.add((start[0], start[1]))
        while queue:
            i, j = queue.pop()

            if (i, j) in found:
                continue
            found.add((i, j))

            if [i, j] == destination:
                return True

            for dx, dy in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
                x, y = i, j
                while isValid(x+dx, y+dy):
                    x += dx
                    y += dy
                queue.add((x, y))

        return False
