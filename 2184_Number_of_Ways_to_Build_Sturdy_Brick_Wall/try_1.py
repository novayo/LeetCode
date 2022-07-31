import functools
class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        '''
        unqiue bricks
        same bricks should not be put at adjacent rows => O(10)
        return (how many ways we can build a sturdy wall) % (10**9+7)
        
        row <= 100
        width <= 10
        len(bricks) <= 10
        
        1. 
        => all_combinations_list = generate all combinations by (width, bricks)
        => recr() => get all answers by all_combinations
        
        [gen all combinations]
        memo
        recr(remain_width):
            if remain_width == 0:
                return [[]]
            if remain_width < 0:
                return []
            
            ret = []
            for i in range(len(bricks)):
                for ret_list in recr(remain_width - bricks[i]):
                    ret.append([bricks[i]] + ret_list)
            return ret
        
        [get answer]
        O(height * 10 * )
        memo[row, pre_idx] = previous answer
        recr(row, pre_idx):
            if row >= height:
                return 0
            
            ret = 0
            loop all_combinations_list => cur_idx:
                check if comb[cur_idx] is adjacent rows with comb[pre_idx] => continue if yes
                ret += recr(row+1, cur_idx)
            return ret
            
        
        2. brute force
        recursion => find all answers
        
        memo[row, tuple] = number of answer of this combination
        recr(row, previous_answer_tuple):
            if row >= height:
                return 0
        '''
        @functools.lru_cache(None)
        def is_adjacency_row(i, j):
            prefix = set()
            cur = 0
            for val in all_combinations[i][:-1]:
                cur += val
                prefix.add(cur)
            
            cur = 0
            for val in all_combinations[j][:-1]:
                cur += val
                if cur in prefix:
                    return True
            return False
            
        
        @functools.lru_cache(None)
        def gen_combinations(remain_width):
            if remain_width == 0:
                return [[]]
            if remain_width < 0:
                return []
            
            ret = []
            for i in range(len(bricks)):
                for ret_list in gen_combinations(remain_width - bricks[i]):
                    ret.append([bricks[i]] + ret_list)
            return ret
        
        @functools.lru_cache(None)
        def recr(row, pre_idx):
            if row >= height:
                return 1
            
            ret = 0
            for i in avaliable[pre_idx]:
                ret += recr(row+1, i) % MOD
            return ret % MOD
        
        def gen_avaliable():
            ret_d = collections.defaultdict(list)
            for i in range(len(all_combinations)):
                for j in range(len(all_combinations)):
                    _i, _j = sorted([i, j])
                    if not is_adjacency_row(_i, _j):
                        ret_d[i].append(j)
            return ret_d
        
        all_combinations = gen_combinations(width)
        avaliable = gen_avaliable()
        MOD = 10**9 + 7
        
        ret = 0
        for i in range(len(all_combinations)):
            ret += recr(1, i) % MOD
        return ret % MOD

