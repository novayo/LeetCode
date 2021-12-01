class Solution:
    def expand(self, s: str) -> List[str]:
        # preprocess
        l = []
        
        stack = []
        for _s in s:
            if _s == '}':
                tmp = []
                while stack[-1] != '{':
                    string = stack.pop()
                    if string != ',':
                        tmp.append(string)
                stack.pop()
                l.append(sorted(tmp))
            elif _s == '{' or len(stack) > 0:
                stack.append(_s)
            else:
                l.append([_s])
        '''
        s = "{a,b}c{d,e}f"
        l = [[a,b], [c], [d,e], [f]]
        '''
        
        def dfs(index):
            if index >= len(l):
                return ['']
            
            ret = []
            next_strings = dfs(index+1)
            for string in l[index]:
                for next_string in next_strings:
                    ret.append(string + next_string)
            return ret
        
        return dfs(0)
