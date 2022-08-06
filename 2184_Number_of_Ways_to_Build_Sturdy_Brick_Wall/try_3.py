class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        def findAllCombs(width):
            if width == 0:
                return [[]]
            elif width < 0:
                return []
            
            ret = []
            for brick in bricks:
                for ret_list in findAllCombs(width - brick):
                    ret.append([brick] + ret_list)
            return ret
        
        def findAllAdjacency(combs):
            # find all presums
            presums = []
            for comb in combs:
                presums.append([])
                cur_sum = 0
                for val in comb:
                    cur_sum += val
                    presums[-1].append(cur_sum)
            
            # find valid adjacency
            ret_d = collections.defaultdict(list)
            ret_d[-1] = [i for i in range(len(combs))]
            for i in range(len(combs)):
                presum_i_set = set()
                for val in presums[i][:-1]:
                    presum_i_set.add(val)
                
                for j in range(len(combs)):
                    if all([val not in presum_i_set for val in presums[j][:-1]]):
                        ret_d[i].append(j)
            return ret_d
        
        @functools.lru_cache(None)
        def recr(i, pre):
            if i >= height:
                return 1
            
            return sum([recr(i+1, nei) for nei in valid_adjacency[pre]])
        
        all_combs = findAllCombs(width)
        valid_adjacency = findAllAdjacency(all_combs)
        return recr(0, -1) % (10**9+7)

