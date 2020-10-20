class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        '''
        bfs
        找出所有的0的位置，分別丟入queue中
        pop出來將周圍是inf的值改掉即可，改掉了再丟進queue，沒改的不用丟
        '''
        if rooms == []:
            return
        
        height = len(rooms)
        width = len(rooms[0])
        queue = collections.deque()
        
        for x in range(height):
            for y in range(width):
                if rooms[x][y] == 0:
                    queue.append((x, y, 0))
        
        while queue:
            x, y, val = queue.popleft()
            
            for next_x, next_y in [x-1, y], [x, y-1], [x+1, y], [x, y+1]:
                if 0 <= next_x < height and 0 <= next_y < width and rooms[next_x][next_y] == 2147483647:
                    rooms[next_x][next_y] = val + 1
                    queue.append((next_x, next_y, val + 1))
