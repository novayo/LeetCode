class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        height = len(maze)
        width = len(maze[0])
        
        found = set()
        found.add((start[0], start[1]))
        
        queue = collections.deque()
        queue.appendleft((start[0], start[1]))
        
        while queue:
            x, y = queue.pop()
            
            
            if [x, y] == destination:
                return True
            
            # top
            i = x
            while i >= 0 and maze[i][y] == 0:
                i -= 1
            i += 1
            
            if (i, y) not in found:
                found.add((i, y))
                queue.appendleft((i, y))
            
            # right
            j = y
            while j < width and maze[x][j] == 0:
                j += 1
            j -= 1
            
            if (x, j) not in found:
                found.add((x, j))
                queue.appendleft((x, j))
            
            # down
            i = x
            while i < height and maze[i][y] == 0:
                i += 1
            i -= 1
            
            if (i, y) not in found:
                found.add((i, y))
                queue.appendleft((i, y))
            
            # left
            j = y
            while j >= 0 and maze[x][j] == 0:
                j -= 1
            j += 1
            
            if (x, j) not in found:
                found.add((x, j))
                queue.appendleft((x, j))
            
        return False

