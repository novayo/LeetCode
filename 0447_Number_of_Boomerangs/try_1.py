class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(pos1, pos2):
            return (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2
        
        
        table = {}
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = distance(points[i], points[j])
                
                if i not in table: table[i] = collections.defaultdict(int)
                if j not in table: table[j] = collections.defaultdict(int)
                
                table[i][dist] += 1
                table[j][dist] += 1
        
        ans = 0
        for i in range(len(points)):
            for dist, value in table.get(i, {}).items():
                if dist > 0 and value >= 2:
                    ans += value * (value-1)
        
        return ans
