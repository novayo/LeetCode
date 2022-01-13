class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        先排滿，再扣除
        
        若相同個數
        AAABBB
        => A .. A .. A
        => A B. A B. AB => idle一樣是扣除A-1個
        '''
        counter = collections.Counter(tasks)
        
        idle = 0
        max = 0
        for i, (key, count) in enumerate(sorted(counter.items(), key=lambda x: x[1], reverse=True)):
            if i == 0:
                idle += (count-1)*n
                max = count
            else:
                idle -= min(max-1, count)
            
            if idle < 0:
                idle = 0
                break
        
        return idle + len(tasks)
