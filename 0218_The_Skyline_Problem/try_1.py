class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings.sort()
        
        valid_x = set()
        for x1, x2, _ in buildings:
            valid_x.add(x1)
            valid_x.add(x2)
        
        ans = []
        hq = []
        i = 0
        for x in sorted(valid_x):
            while i < len(buildings) and buildings[i][0] <= x:
                heapq.heappush(hq, (-buildings[i][2], buildings[i][1]))
                i += 1
            
            while hq and hq[0][1] <= x:
                heapq.heappop(hq)
            
            h = 0
            if hq:
                h = -hq[0][0]
                
            if not ans or ans[-1][1] != h:
                ans.append([x, h])
        
        return ans
