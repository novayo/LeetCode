class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        all_x = set()
        L = []
        for x1, y1, x2, y2 in rectangles:
            all_x.add(x1)
            all_x.add(x2)
            L.append([y1, x1, x2, 1])
            L.append([y2, x1, x2, -1])
        all_x = sorted(all_x)
        L.sort()
        
        x_indices = {v: i for i, v in enumerate(all_x)}
        count = [0] * len(x_indices)
        
        cur_y = length = area = 0
        for y, x1, x2, delta in L:
            area = (area + (y-cur_y) * length) % MOD
            cur_y = y
            
            for i in range(x_indices[x1], x_indices[x2]):
                count[i] += delta
            
            length = 0
            for i in range(len(all_x)-1):
                x = all_x[i]
                if count[x_indices[x]] > 0:
                    length += all_x[i+1] - all_x[i]
        return area
        
