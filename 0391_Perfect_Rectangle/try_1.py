class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        # O(n) time / O(n) space
        #  - where n is the length of the input array
        LD, RU = [float('inf'), float('inf')], [-float('inf'), -float('inf')]
        counter = collections.Counter()
        cur_area_sum = 0
        
        for x1, y1, x2, y2 in rectangles:
            # 邊找最左下，最右上 => 依照x為準
            LD[0] = min(LD[0], x1)
            LD[1] = min(LD[1], y1)
            RU[0] = max(RU[0], x2)
            RU[1] = max(RU[1], y2)
            
            # dict 紀錄四頂點出現的次數
            counter[x1, y1] += 1
            counter[x1, y2] += 1
            counter[x2, y1] += 1
            counter[x2, y2] += 1
            
            # 計算面積總合
            cur_area_sum += (x2 - x1) * (y2 - y1)
        
        # 是否重疊、缺少
        if cur_area_sum != (RU[0] - LD[0]) * (RU[1] - LD[1]):
            return False
        
        if 3 in counter.values():
            return False
        
        # 是否只有四個點是1 & 4個點是左下右上的
        return collections.Counter(counter.values())[1] == 4 and counter[LD[0], LD[1]] == counter[LD[0], RU[1]] == counter[RU[0], LD[1]] == counter[RU[0], LD[1]] == 1
