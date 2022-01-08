class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        '''
        1 * C2_1 * C1_1
        
        '''
        def distance(p1, p2):
            return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
        
        
        n = len(points)
        
        # find all distance
        dist = {}
        for i in range(n):
            for j in range(i+1, n):
                p1 = tuple(points[i])
                p2 = tuple(points[j])
                
                if p1 not in dist:
                    dist[p1] = collections.defaultdict(int)
                if p2 not in dist:
                    dist[p2] = collections.defaultdict(int)
                
                dist[p1][distance(p1, p2)] += 1
                dist[p2][distance(p1, p2)] += 1
        
        
        # get ans
        ans = 0
        for point, counter_dict in dist.items():
            for d, count in counter_dict.items():
                if count >= 2:
                    ans += count * (count-1)
        
        return ans