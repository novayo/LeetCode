# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        
        matrix = [[-1] * n for _ in range(m)]
        face = RIGHT
        x = y = 0
        cache = set()
        
        while head:
            matrix[x][y] = head.val
            cache.add((x, y))
            
            if face == RIGHT:
                if y+1 >= n or (x, y+1) in cache:
                    face = DOWN
                    x += 1
                else:
                    y += 1
            elif face == DOWN:
                if x+1 >= m or (x+1, y) in cache:
                    face = LEFT
                    y -= 1
                else:
                    x += 1
            elif face == LEFT:
                if y-1 < 0 or (x, y-1) in cache:
                    face = UP
                    x -= 1
                else:
                    y -= 1
            else:
                if x-1 < 0 or (x-1, y) in cache:
                    face = RIGHT
                    y += 1
                else:
                    x -= 1
            
            head = head.next
            
        return matrix