class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        '''
        do bfs from all gates to update min value
        '''
        
        def bfs(i, j):
            queue = [(i, j)]
            found = set([(i, j)])
            layer = 1
            
            while queue:
                tmp = []
                
                while queue:
                    i, j = queue.pop()
                    
                    for x, y in [i-1, j], [i+1, j], [i, j-1], [i, j+1]:
                        if x < 0 or y < 0 or x >= len(rooms) or y >= len(rooms[0]) \
                           or rooms[x][y] == -1 or (x, y) in found \
                           or rooms[x][y] <= layer:
                            continue
                        found.add((x, y))
                        tmp.append((x, y))
                        rooms[x][y] = min(rooms[x][y], layer)
                
                queue = tmp
                layer += 1
        
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == 0:
                    bfs(i, j)
