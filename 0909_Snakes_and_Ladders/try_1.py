class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        '''
        電梯：往上走
        電鰻：往下走
        '''
        n = len(board)
                
        # 編號
        table = {}
        
        direction = True
        i, j, number = n-1, 0, 1
        while number <= n**2:
            table[number] = (i, j)
            
            number += 1
            if direction:
                j += 1
                if j >= n:
                    i, j = i-1, n-1
                    direction = False
            else:
                j -= 1
                if j < 0:
                    i, j = i-1, 0
                    direction = True
        
        # bfs
        queue = collections.deque()
        queue.appendleft((1, 0)) # pos, step
        found = set([1])        
        
        while queue:
            number, step = queue.pop()
            
            if number == n**2:
                return step
            
            for score in range(1, 7):
                next_number = number + score
                
                if next_number > n**2:
                    break
                
                i, j = table[next_number]
                if board[i][j] > -1:
                    next_number = board[i][j]
                
                if next_number in found:
                    continue
                found.add(next_number)
                queue.appendleft((next_number, step+1))
        
        return -1
                
                
