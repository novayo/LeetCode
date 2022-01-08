RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width = len(matrix[0])
        height = len(matrix)
        
        found = set()
        pos = [0, 0]
        index_dir = 0
        
        ans = []
        while True:
            ans.append(matrix[pos[0]][pos[1]])
            found.add(tuple(pos))
            
            for retry in range(4):
                new_pos = [pos[0], pos[1]]
                
                if index_dir == RIGHT:
                    new_pos[1] += 1
                elif index_dir == DOWN:
                    new_pos[0] += 1
                elif index_dir == LEFT:
                    new_pos[0] -= 1
                else:
                    new_pos[1] -= 1

                if new_pos[0] < 0 or new_pos[0] >= height or new_pos[1] < 0 or new_pos[1] >= width or tuple(new_pos) in found:
                    index_dir = (index_dir+1) % 4
                    if retry + 1 == 4:
                        return ans
                else:                
                    pos[0], pos[1] = new_pos[0], new_pos[1]
                    break
                
            
        