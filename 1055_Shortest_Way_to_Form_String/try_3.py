class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        index_mapping = collections.defaultdict(list)
        for i in range(len(source)):
            index_mapping[source[i]].append(i)
        
        i = ans = 0
        cur_index_in_source = -1
        
        while i < len(target):
            if target[i] not in index_mapping:
                return -1
            
            index = bisect.bisect_right(index_mapping[target[i]], cur_index_in_source)
            
            if index >= len(index_mapping[target[i]]):
                cur_index_in_source = index_mapping[target[i]][0]
                ans += 1
            elif index_mapping[target[i]][index] > cur_index_in_source:
                cur_index_in_source = index_mapping[target[i]][index]
            
            i += 1
        
        return ans+1
