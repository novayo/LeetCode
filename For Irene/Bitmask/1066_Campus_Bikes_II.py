class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def dist(pos1, pos2):
            return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])
        
        memo = {}
        def recr(index, bitmask=0):
            if index >= len(workers):
                return 0
            
            if bitmask not in memo:
                ret = float('inf')
                for i in range(len(bikes)):
                    if bitmask & (1<<i) != 0:
                        continue
                    ret = min(ret, dist(workers[index], bikes[i]) + recr(index+1, bitmask | (1<<i)))
                memo[bitmask] = ret
            return memo[bitmask]
        
        return recr(0)
