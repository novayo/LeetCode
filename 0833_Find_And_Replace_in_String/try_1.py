class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = []
        ptr = 0
        
        tmp = []
        for index, source, target in zip(indices, sources, targets):
            tmp.append((index, source, target))
        
        tmp.sort()
        
        for i in range(len(tmp)):
            index, source, target = tmp[i]
        
            if ptr >= len(s):
                break
        
            if ptr < index:
                ans.append(s[ptr:index])
                ptr = index
            
            if s[ptr:ptr+len(source)] == source:
                ans.append(target)
                ptr = ptr+len(source)
            else:
                ans.append(s[ptr:ptr+len(source)])
                ptr = ptr+len(source)
        
        
        ans.append(s[ptr:])
        
        return ''.join(ans)

        
