class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        greedy => 拿最長的出來 先填好空格，後續的不用管
        '''
        
        counter = collections.Counter(tasks)
        _list = sorted(counter.values(), reverse=True)
        
        valid_spaces = _list[0]-1
        idles = valid_spaces * n
        for count in _list[1:]:
            idles -= min(valid_spaces, count)
            if idles < 0:
                idles = 0
                break
        
        return idles + len(tasks)
