class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        cache = collections.Counter()
        for s, e, v in segments:
            cache[s] += v
            cache[e] -= v
        
        ans = []
        cur = 0
        s = 1
        for e in sorted(cache.keys()):
            if cur > 0:
                ans.append([s, e, cur])
            cur += cache[e]
            s = e
        return ans