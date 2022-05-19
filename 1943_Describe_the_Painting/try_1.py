class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        mp = collections.defaultdict(int)
        for s, e, p in segments:
            mp[s] += p
            mp[e] -= p
        
        ret = []
        pre_time = 0
        cur = 0
        for time in sorted(mp.keys()):
            if cur > 0:
                ret.append([pre_time, time, cur])
            
            cur += mp[time]
            pre_time = time
        return ret
