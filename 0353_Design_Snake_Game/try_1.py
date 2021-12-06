'''
1. 只記錄轉彎處
2. 
用dict存 並 編號（當前時間）（key: time, value: pos），set 存pos方邊in dict
編號超過就del，只需紀錄最小值即可
每動一步時間+1
若吃到食物則新增食物位置
超出邊界 或 in dict則return -1 => game flag
'''
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        
        self.score = 0
        self.food_index = 0
        self.gameLive = True
        self.min_time = 0
        self.time = 0
        self.time_mapping = {}
        self.body_set = set()
        self.cur_pos = [0, 0]

    # O(1)
    def move(self, direction: str) -> int:
        self.make_move(direction)
        self.check_pos()
        self.time += 1
        
        if self.gameLive == False:
            return -1
        
        if not self.eat_food():
            self.min_time += 1
            if self.score > 0:
                pre_x, pre_y = self.time_mapping[self.min_time]
                self.body_set.remove((pre_x, pre_y))
                del self.time_mapping[self.min_time]
        
        if self.score > 0:
            self.time_mapping[self.time] = (self.cur_pos[0], self.cur_pos[1])
            self.body_set.add((self.cur_pos[0], self.cur_pos[1]))
        
        return self.score
        
    def make_move(self, direction):
        if direction == "R":
            self.cur_pos[1] += 1
        elif direction == "D":
            self.cur_pos[0] += 1
        elif direction == "U":
            self.cur_pos[0] -= 1
        else:
            self.cur_pos[1] -= 1

    def check_pos(self):
        x, y = self.cur_pos
        
        if x < 0 or y < 0 or x >= self.height or y >= self.width or (x, y) in self.body_set:
            self.gameLive = False
        
    def eat_food(self):
        x, y = self.cur_pos
        if self.food_index < len(self.food) and [x, y] == self.food[self.food_index]:
            self.food_index += 1
            self.score += 1
            return True
        else:
            return False
        
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
