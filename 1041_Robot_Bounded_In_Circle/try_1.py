class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        '''
        分兩種情況
        1. 走完一輪後，回到原點
        2. 走完一輪後，方向不向上
            => 方向不向上 => 多跑幾次就會回來了 (每次方向都會改變)
            => 方向向上 => 之後怎麼跑都會往上跑
        '''
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3
        
        def next_(pos, face, instruction):
            shift_x, shift_y = 0, 0
            
            if instruction == "G":
                if face == UP:
                    shift_x = -1
                elif face == RIGHT:
                    shift_y = 1
                elif face == DOWN:
                    shift_x = 1
                elif face == LEFT:
                    shift_y = -1
            elif instruction == "L":
                if face == UP:
                    face = LEFT
                elif face == RIGHT:
                    face = UP
                elif face == DOWN:
                    face = RIGHT
                elif face == LEFT:
                    face = DOWN
            elif instruction == "R":
                if face == UP:
                    face = RIGHT
                elif face == RIGHT:
                    face = DOWN
                elif face == DOWN:
                    face = LEFT
                elif face == LEFT:
                    face = UP
            
            pos[0] += shift_x
            pos[1] += shift_y
            return face, pos
        
        pos = [0, 0]
        face = UP
        for i in instructions:
            face, pos = next_(pos, face, i)
        
        if (pos == [0, 0]) or (face != UP):
            return True
        else:
            return False