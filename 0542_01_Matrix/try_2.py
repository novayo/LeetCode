class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        找1，若1的上下左右都大於等於自己(代表周圍沒有0)，則自己加一，再丟回去queue內
        '''
        height = len(matrix)
        width = len(matrix[0])
        queue = collections.deque()
        
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 1:
                    queue.append((i, j))
        
        while queue:
            i, j = queue.popleft()
            
            
            if (i==0 or matrix[i-1][j] >= matrix[i][j]) and \
               (j==0 or matrix[i][j-1] >= matrix[i][j]) and \
               (i==height-1 or matrix[i+1][j] >= matrix[i][j]) and \
               (j==width-1 or matrix[i][j+1] >= matrix[i][j]):
                matrix[i][j] += 1
                queue.append((i, j))
        
        return matrix