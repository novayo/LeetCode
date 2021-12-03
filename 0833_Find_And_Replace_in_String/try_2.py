class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        mapping = {}
        success = {}
        
        # preprocess + looking for mapping s
        for i in range(len(indices)):
            index = indices[i]
            source = sources[i]
            target = targets[i]
            
            mapping[index] = source
            
            if s[index : index+len(source)] == source:
                success[index] = target
        
        # get answer
        ans = []
        i = 0
        while i < len(s):
            if i in success:
                ans.append(success[i])
                i += len(mapping[i])
            else:
                ans.append(s[i])
                i += 1
        
        return ''.join(ans)
            
