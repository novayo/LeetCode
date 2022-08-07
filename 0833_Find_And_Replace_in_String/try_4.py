class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        tmp = [(i, s, t) for i, s, t in zip(indices, sources, targets)]
        tmp.sort()
        
        ans = ''
        k = len(indices)
        end = len(s)
        
        for j in range(k-1, -1, -1):
            i, source, target = tmp[j]
            
            if s[i: i+len(source)] != source:
                continue
            
            ans = target + s[i+len(source): end] + ans
            end = i
            
        if end > 0:
            ans = s[:end] + ans
        return ans
        
