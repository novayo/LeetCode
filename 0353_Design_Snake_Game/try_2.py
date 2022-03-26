class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.f_index = 0
        self.body = collections.deque([(0, 0)])
        self.b_set = set([(0, 0)])
        self.game_alive = True

    def move(self, direction: str) -> int:
        if not self.game_alive:
            return -1
        
        # get next pos
        x, y = self.get_next_pos(direction)
        
        # not get food => pop body
        if not self.ate(x, y):
            self.b_set.remove(self.body.popleft())
        
        # judge is valid or not
        if not (0 <= x < self.height) or not (0 <= y < self.width) or (x, y) in self.b_set:
            self.game_alive = False
            return -1
        
        self.body.append((x, y))
        self.b_set.add((x, y))
        return self.f_index
        
    
    def ate(self, x, y):
        if self.f_index >= len(self.food):
            return False
        
        if self.food[self.f_index] == [x, y]:
            self.f_index += 1
            return True
        else:
            return False
    
    def get_next_pos(self, direction):
        x, y = self.body[-1]
        
        if direction == 'U':
            return x-1, y
        elif direction == 'R':
            return x, y+1
        elif direction == 'D':
            return x+1, y
        else:
            return x, y-1
    

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
