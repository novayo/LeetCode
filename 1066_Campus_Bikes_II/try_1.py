class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def Manhattan(pos1, pos2):
            return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
        
        table = collections.defaultdict(list)
        
        # build table by worker & Manhattan
        for i in range(len(workers)):
            worker = workers[i]
            
            for j in range(len(bikes)):
                bike = bikes[j]
                table[i].append((Manhattan(worker, bike), j))
            
        def backtracking(index, bitmask=0):
            if index >= len(workers):
                return 0
            
            if bitmask in memo:
                return memo[bitmask]
            
            ret = float('inf')
            for i in range(len(table[index])):
                dist, bike_index = table[index][i]
                
                mask = 2**bike_index
                
                if mask & bitmask == 0:
                    ret = min(ret, dist + backtracking(index+1, mask | bitmask))
            
            memo[bitmask] = ret
            return memo[bitmask]
            
        memo = {}
        return backtracking(0)
