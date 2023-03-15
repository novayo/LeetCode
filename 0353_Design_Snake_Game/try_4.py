'''
move => push head, pop tail => queue
eat => push head
'''
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.game_status = True
        self.width = width
        self.height = height
        self.body_que = collections.deque()
        self.body_set = set()
        self.food = food
        self.food_index = 0
        
        # init
        self.x, self.y = 0, 0
        self.body_que.appendleft((self.x, self.y))
        self.body_set.add((self.x, self.y))

    def is_eat(self):
        if self.food_index >= len(self.food):
            return False
        
        food_x = self.food[self.food_index][0]
        food_y = self.food[self.food_index][1]
        if food_x == self.x and food_y == self.y:
            self.food_index += 1
            return True
        return False
    
    def is_valid(self):
        # out of bound
        if not (0 <= self.x < self.height and 0 <= self.y < self.width):
            return False
        
        # occupies its body
        return (self.x, self.y) not in self.body_set
    
    def move(self, direction: str) -> int:
        if self.game_status is False:
            return -1
        
        if direction == "U":
            self.x -= 1
        elif direction == "R":
            self.y += 1
        elif direction == "D":
            self.x += 1
        else:
            self.y -= 1
        
        # move or eat
        if not self.is_eat():
            (_x, _y) = self.body_que.pop()
            self.body_set.remove((_x, _y))
        
        # 如果不合法
        if not self.is_valid():
            self.game_status = False
            return -1
        
        self.body_que.appendleft((self.x, self.y))
        self.body_set.add((self.x, self.y))
        return len(self.body_que) - 1
        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)