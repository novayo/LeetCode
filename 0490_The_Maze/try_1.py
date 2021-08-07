class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        queue = collections.deque()
        found = set()
        
        # init
        queue.appendleft(start)
        
        # bfs
        while queue:
            x, y = queue.pop()
            
            if [x, y] == destination:
                return True
            
            found.add((x, y))
            
            # up
            for i in range(len(maze)):
                if x-i-1 < 0 or maze[x-i-1][y] == 1: # 走到底了
                    if (x-i, y) not in found:
                        queue.append((x-i, y))
                    break
                    
            # down
            for i in range(len(maze)):
                if x+i+1 >= len(maze) or maze[x+i+1][y] == 1: # 走到底了
                    if (x+i, y) not in found:
                        queue.append((x+i, y))
                    break
            
            # left
            for i in range(len(maze[0])):
                if y-i-1 < 0 or maze[x][y-i-1] == 1: # 走到底了
                    if (x, y-i) not in found:
                        queue.append((x, y-i))
                    break
            
            # right
            for i in range(len(maze[0])):
                if y+i+1 >= len(maze[0]) or maze[x][y+i+1] == 1: # 走到底了
                    if (x, y+i) not in found:
                        queue.append((x, y+i))
                    break
        
        return False
