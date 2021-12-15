class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        [1,2,3,5,6,7,8,10,12,16]
           2     6
        
        start => bisect_left
        end   => bisect_right
        
        if start => even => 取代
                 => odd  => 不變
        if end   => even => 把i~j-1替換掉，並補上end
                 => odd  => 不變
        '''
        
        l = []
        for interval in intervals:
            l += interval
        
        left = bisect.bisect_left(l, newInterval[0])
        right = bisect.bisect_right(l,newInterval[1])
        
        tmp = []
        if left % 2 == 0:
            tmp.append(newInterval[0])
        if right % 2 == 0:
            tmp.append(newInterval[1])
        
        l[left:right] = tmp
        
        ret = []
        for i in range(len(l) // 2):
            ret.append(l[i*2: i*2+2])
        return ret
            
