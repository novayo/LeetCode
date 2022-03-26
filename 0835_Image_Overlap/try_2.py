class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        '''
        img2的 (1, 1) & (1, 2) 移動到 img1的(0, 0) & (0, 1) 位移相等
        
        注意：不能只考慮距離，因為可以往左上5格或右下5格，所以要記得位移
        '''
        height = len(img1)
        width = len(img1[0])
        
        t1 = []
        t2 = []
        
        for i in range(height):
            for j in range(width):
                if img1[i][j] == 1:
                    t1.append((i, j))
                if img2[i][j] == 1:
                    t2.append((i, j))
        
        table = collections.defaultdict(int)
        for _t1 in t1:
            for _t2 in t2:
                table[(_t1[0]-_t2[0], _t1[1]-_t2[1])] += 1
        
        if not table:
            return 0
        return max(table.values())
        
        
