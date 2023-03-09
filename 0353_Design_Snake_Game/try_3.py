class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.game_state = True
        self.i = 0
        self.j = 0
        self.body_set = set()
        self.body_set.add((0, 0))
        self.body_que = collections.deque()
        self.body_que.appendleft((0, 0))
        
        self.food_list = food
        self.food_idx = 0

    def move_pos(self, direction):
        if direction == "U":
            self.i -= 1
        elif direction == "R":
            self.j += 1
        elif direction == "D":
            self.i += 1
        else:
            self.j -= 1
            
    def check_if_out_of_bound(self):
        if not (0 <= self.i <= self.height-1 and 0 <= self.j <= self.width-1):
            return True
        return False
    
    def is_eat_food(self):
        if self.food_idx >= len(self.food_list):
            return False
        return self.food_list[self.food_idx] == [self.i, self.j]
    
    def hit_body(self):
        return (self.i, self.j) in self.body_set
    
    def move(self, direction: str) -> int:
        if self.game_state == False:
            return -1
        
        self.move_pos(direction)
        
        if self.check_if_out_of_bound():
            self.game_state = False
            return -1
        
        if self.is_eat_food():
            self.food_idx += 1
        else:
            self.body_set.remove(self.body_que.pop())
            
        if self.hit_body():
            self.game_state = False
            return -1
        
        self.body_que.appendleft((self.i, self.j))
        self.body_set.add((self.i, self.j))
        
        return len(self.body_que) - 1
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
