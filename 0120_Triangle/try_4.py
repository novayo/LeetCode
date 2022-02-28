class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        dp
        '''
        def get(i, j):
            if i < 0 or j < 0 or i >= len(triangle) or j >= len(triangle[i]):
                return float('inf')
            return triangle[i][j]
        
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(get(i-1, j), get(i-1, j-1))
        
        return min(triangle[-1])
