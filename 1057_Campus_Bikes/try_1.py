class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        ans = [0] * len(workers)
        
        d_w_b = []
        for w, worker in enumerate(workers):
            for b, bike in enumerate(bikes):
                d_w_b.append([self.Manhattan(worker, bike), w, b])
        
        d_w_b.sort()
        used_worker = set()
        used_bike = set()
        
        for pair in d_w_b:
            if pair[1] in used_worker or pair[2] in used_bike:
                continue
            else:
                ans[pair[1]] = pair[2]
                used_worker.add(pair[1])
                used_bike.add(pair[2])
            
        return ans
        
        
    def Manhattan(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
