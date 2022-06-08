class Solution:
    def encode(self, s: str) -> str:
        memo = {}
        def dfs(string):
            
            if string not in memo:
                ret = []

                # find pattern
                min_length = -1
                for length in range(1, len(string)):
                    _s = string[:length]

                    if len(string) % length == 0 and _s * (len(string) // length) == string:
                        min_length = length
                        break

                # encode
                if min_length != -1:
                    ptn = string[:min_length]
                    ret.append(f'{len(string) // len(ptn)}[{dfs(ptn)}]')
                else:
                    ret.append(string)

                # not encode
                for i in range(1, len(string)):
                    ret.append(dfs(string[:i]) + dfs(string[i:]))
                
                memo[string] = min(ret, key=len)
                
            return memo[string]
        
        return dfs(s)