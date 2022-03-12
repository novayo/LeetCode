class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        '''
        看是否可以 兩兩一組
        '''
        counter = collections.Counter(arr)
        
        for a, count in sorted(counter.items(), key=lambda x: x[0]):
            if a == 0:
                if counter[0] % 2 == 1:
                    return False
                else:
                    counter[0] = 0
            elif a*2 in counter:
                minus = min(counter[a*2], counter[a])
                counter[a*2] -= minus
                counter[a] -= minus
        
        return all([x == 0 for x in counter.values()])

