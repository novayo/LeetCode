class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        max_heap = []
        i = 0
        
        while i < n:
            while i + 1 < n and heights[i] >= heights[i+1]:
                i += 1
            
            if i == n-1:
                break
            
            pay = heights[i+1] - heights[i]
            heapq.heappush(max_heap, -pay)
            
            if bricks < pay and ladders > 0:
                ladders -= 1
                bricks += -heapq.heappop(max_heap)
                
            if bricks >= pay:
                bricks -= pay
            else:
                break
                
            i += 1
            
        return i
            