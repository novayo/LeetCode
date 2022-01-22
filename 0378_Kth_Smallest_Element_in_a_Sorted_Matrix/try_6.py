class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        height = len(matrix)
        width = len(matrix[0])
        index_of_row = [0] * height
        
        heap = []
        for i in range(height):
            x, y = i, index_of_row[i]
            heap.append((matrix[x][y], i))
        heapq.heapify(heap)
        
        count = 1
        while heap:
            value, row = heapq.heappop(heap)
            
            if count == k:
                return value
            count += 1
            index_of_row[row] += 1
            
            if index_of_row[row] < width:
                heapq.heappush(heap, (matrix[row][index_of_row[row]], row))
        
        return -1
            
        
