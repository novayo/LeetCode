class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        '''
        two pointer
            -> if len(query) < len(pattern) => False
            -> if query[i] is lower and pattern[j] is lower
                -> i += 1
            -> if query[i] is upper and pattern[j] is lower
                -> False
            -> if query[i] is lower and pattern[j] is upper
                -> i += 1
            -> if query[i] is upper and pattern[j] is upper
                -> return False or continue
        '''
        ans = [False] * len(queries)
        for ind, query in enumerate(queries):
            
            if len(query) < len(pattern):
                continue
            
            i = j = 0
            while i < len(query) and j < len(pattern):
                q, p = query[i], pattern[j]
                
                if q == p:
                    i, j = i+1, j+1
                elif q.isupper():
                    break
                else:
                    i += 1
            
            # if not satisfy pattern
            if j < len(pattern):
                continue
            
            # if there's a upper in query => False
            while i < len(query) and query[i].islower():
                i += 1
            
            if i >= len(query):
                ans[ind] = True
        
        return ans
        
