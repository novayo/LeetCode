class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        matrix1 = [[0 for _ in range(sideLength)] for _ in range(sideLength)]

        for i in range(height):
            for j in range(width):
                matrix1[i%sideLength][j%sideLength] -= 1
        
        heap = []
        for i in range(sideLength):
            for j in range(sideLength):
                heap.append((matrix1[i][j], i, j))
        heapq.heapify(heap)

        matrix2 = [[0 for _ in range(sideLength)] for _ in range(sideLength)]
        for _ in range(maxOnes):
            _, i, j = heapq.heappop(heap)
            matrix2[i][j] = 1

        ans = 0
        for i in range(height):
            for j in range(width):
                ans += matrix2[i % sideLength][j % sideLength] == 1

        return ans