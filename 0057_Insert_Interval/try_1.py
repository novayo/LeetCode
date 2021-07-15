class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        _list = []
        for l in intervals:
            _list += l
        
        left = bisect.bisect_left(_list, newInterval[0])
        right = bisect.bisect_right(_list, newInterval[1])
        
        new = []
        if left % 2 == 0:
            new.append(newInterval[0])
        if right % 2 == 0:
            new.append(newInterval[1])
        _list[left:right] = new
        
        ret = []
        i = 0
        tmp = []
        while i < len(_list):
            tmp.append(_list[i])
            if i%2 == 1:
                ret.append(tmp.copy())
                tmp.clear()
            i += 1
        return ret
