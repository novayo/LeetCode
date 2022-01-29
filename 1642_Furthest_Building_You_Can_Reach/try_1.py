class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        '''
        1. top-down recursion + memo => TLE
        2. use bricks only and use ladders to replace one of the highest jump
        '''
        
        heap = []
        index = 0
        
        while index < len(heights) and (bricks > 0 or ladders > 0):
            # go until reach wall
            while index < len(heights) - 1 and heights[index] >= heights[index+1]:
                index += 1
            
            # if reach end
            if index >= len(heights)-1:
                break
            
            consume_bricks = heights[index+1] - heights[index]
            heapq.heappush(heap, -consume_bricks)
            
            if bricks - consume_bricks >= 0:
                bricks -= consume_bricks
                index += 1
            elif ladders > 0:
                resume_bricks = -heapq.heappop(heap)
                ladders -= 1
                bricks += resume_bricks
                
                if bricks - consume_bricks >= 0:
                    bricks -= consume_bricks
                    index += 1
                else:
                    break
            else:
                break
        
        # go until reach wall
        while index < len(heights) - 1 and heights[index] >= heights[index+1]:
            index += 1
        return index
