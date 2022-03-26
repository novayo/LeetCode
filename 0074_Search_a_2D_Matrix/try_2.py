class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])
        
        # init
        min_heap = []
        for i in range(height):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))
        
        # get answer
        while min_heap:
            num, i, j = heapq.heappop(min_heap)
            
            if num == target:
                return True
            
            if j+1 < width:
                heapq.heappush(min_heap, (matrix[i][j+1], i, j+1))
        
        return False
                
