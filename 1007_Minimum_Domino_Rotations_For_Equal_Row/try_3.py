class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        '''
        O(n) O(n)
        basic idea: 
            -> 是否有文字出現在每一個index上 
                => [set()] * n => 之後union all => 所有可能
                => top = {記錄個數}
                => down= {紀錄個數}
            
            ans 去紀錄最小解
            -> 尋找所有可能 => min(都換到上面(n - 原本在上面的), 都換到下面(n - 原本在下面的))
        '''
        n = len(tops)
        top = collections.defaultdict(int)
        down = collections.defaultdict(int)
        index_set = [set() for i in range(n)]
        
        # init
        for i in range(n):
            top[tops[i]] += 1
            down[bottoms[i]] += 1
            
            index_set[i].add(tops[i])
            index_set[i].add(bottoms[i])
        
        # get possible
        possible = index_set[0]
        for s in index_set[1:]:
            possible &= s
        
        # loop
        ans = float('inf')
        for value in possible:
            ans = min(ans, n - max(top[value], down[value]))
        
        return ans if ans != float('inf') else -1
