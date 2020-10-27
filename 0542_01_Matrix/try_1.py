class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        用0去找最近的1
        '''
        
        height = len(matrix)
        width = len(matrix[0])
        queue = collections.deque()
        visited = set()
        
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        while queue:
            i, j = queue.popleft()
            
            for a, b in [i+1, j], [i-1, j], [i, j+1], [i, j-1]:
                if 0 <= a < height and 0 <= b < width and (a, b) not in visited:
                    matrix[a][b] = matrix[i][j] + 1
                    queue.append((a, b))
                    visited.add((a, b))
        
        return matrix