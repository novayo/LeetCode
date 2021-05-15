class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        '''
        1. 紀錄當前位置，比較目前最小值 => O(n^2)
        *2. 用priority queue，紀錄目前所有可能，並取出最小值，再將此位置周圍加入至queue => O(klogn)
        '''
        length = len(matrix)
        heap = [matrix[0][0]]     # min heap
        location = collections.defaultdict(list) # 紀錄位置
        location[matrix[0][0]].append((0, 0))
        
        ans = -1
        for _ in range(k):
            value = heapq.heappop(heap)
            (x, y) = location[value].pop()
            
            if y == 0 and x + 1 < length:
                heapq.heappush(heap, matrix[x+1][y])
                location[matrix[x+1][y]].append((x+1, y))
            
            if y + 1 < length:
                heapq.heappush(heap, matrix[x][y+1])
                location[matrix[x][y+1]].append((x, y+1))
            
            ans = value
            
        return ans