class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        @functools.lru_cache(None)
        def getAllCombinations(target):
            if target == 0:
                return [[]]
            elif target < 0:
                return []
            
            ret = []
            for brick in bricks:
                for ret_list in getAllCombinations(target-brick):
                    ret.append([brick] + ret_list)
            return ret
        
        def getAllPresum():
            ret = []
            for comb in combs:
                tmp = []
                cur = 0
                for v in comb:
                    cur += v
                    tmp.append(cur)
                ret.append(tmp)
            return ret
        
        def getAllAdjacent():
            ret_d = collections.defaultdict(list)
            ret_d[-1] = [i for i in range(len(combs))]
            
            for i in range(len(combs)):
                p1_set = set()
                for val in presums[i][:-1]:
                    p1_set.add(val)
                
                for j in range(len(combs)):
                    if all([val not in p1_set for val in presums[j][:-1]]):
                        ret_d[i].append(j)
            return ret_d
        
        @functools.lru_cache(None)
        def recr(row, pre):
            if row >= height:
                return 1
            
            ret = 0
            for _next in adjacents[pre]:
                ret += recr(row+1, _next)
            return ret
        
        MOD = 10**9+7
        combs = getAllCombinations(width)
        presums = getAllPresum()
        adjacents = getAllAdjacent()
        return recr(0, -1) % MOD
        
        