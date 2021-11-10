class Solution:
    def nextClosestTime(self, time: str) -> str:
        '''
        找出所有組合
        取出時間差最小的
        '''
        time = time[:2] + time[3:]
        kinds = set([time[0], time[1], time[2], time[3]])
        
        # get all valid combination
        def recr(index=0):
            if index >= 3:
                return list(kinds)
            
            ret = []
            for v in recr(index+1):
                for kind in kinds:
                    tmp = kind + v
                    if len(tmp) == 2 and not (0 <= int(tmp) < 60):
                        continue
                    if len(tmp) == 4 and not (0 <= int(tmp[:2]) < 24):
                        continue
                    ret.append(tmp)
            return ret
            
        all_kinds = recr()
        
        # find next closest time => 分類
        less = '9999'
        greater = '9999'
        for kind in all_kinds:
            for i in range(4):
                if int(time[i]) > int(kind[i]):
                    less = min(less, kind)
                    break
                elif int(time[i]) < int(kind[i]):
                    greater = min(greater, kind)
                    break
        
        ret = time
        if greater != '9999':
            ret = greater
        elif less != '9999':
            ret = less
        
        return ret[:2] + ':' + ret[2:]
        
