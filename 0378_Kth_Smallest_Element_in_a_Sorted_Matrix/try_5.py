class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        height = width = len(matrix)
        indexes = [0] * k
        heap = []
        
        for i in range(height):
            heapq.heappush(heap, (matrix[i][0], i))
        
        ans = 0
        for _ in range(k):
            ans, i = heapq.heappop(heap)
            indexes[i] += 1
            
            if indexes[i] < width:
                heapq.heappush(heap, (matrix[i][indexes[i]], i))
        return ans
