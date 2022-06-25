from sortedcontainers import SortedList

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        '''
        sweep line + heap + greedy
        greedy: y找最遠，確認overlap
        '''
        min_heap = []
        bst = SortedList()
        
        ldx = ldy = float('inf')
        rux = ruy = float('-inf')
        sum_area = 0
        
        for x1, y1, x2, y2 in rectangles:
            sum_area += (x2 - x1) * (y2 - y1)
            ldx = min(ldx, x1)
            ldy = min(ldy, y1)
            rux = max(rux, x2)
            ruy = max(ruy, y2)
            
            heapq.heappush(min_heap, (x1*2+1, -y1, y2))
            heapq.heappush(min_heap, (x2*2, -y1, y2))
            
        while min_heap:
            x, y_start, y_end = heapq.heappop(min_heap)
            y_start *= -1
            
            if x % 2 == 0:
                bst.remove((y_start, y_end))
            else:
                i = bst.bisect_left((y_start, y_end))
                if i > 0 and bst[i-1][1] > y_start:
                    return False
                if i < len(bst) and bst[i][0] < y_end:
                    return False
                bst.add((y_start, y_end))
        return sum_area == (rux - ldx) * (ruy - ldy)
