class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        def Manhattan_Distance(pos1, pos2):
            return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
        
        pair = []
        for i in range(len(workers)):
            for j in range(len(bikes)):
                pair.append((Manhattan_Distance(workers[i], bikes[j]), i, j))
        
        ans = [0] * len(workers)
        pair.sort()
        found_worker = set()
        found_bike = set()
        for d, w, b in pair:
            if w in found_worker or b in found_bike:
                continue
            
            ans[w] = b
            found_worker.add(w)
            found_bike.add(b)
        
        return ans
