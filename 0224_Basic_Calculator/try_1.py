class Solution:
    def calculate(self, s: str) -> int:
        # find pair
        n = len(s)
        pair_index = {}
        stack = []
        for i, _s in enumerate(s):
            if _s == '(':
                stack.append(i)
            elif _s == ')':
                pair_index[stack.pop()] = i
        
        def recr(i, j):
            ans = 0
            cur = '0'
            symbol = ' '
            
            while i <= j:
                if s[i] == ' ':
                    pass
                elif s[i] in '+-':
                    ans += int(symbol + cur)
                    cur = '0'
                    symbol = s[i]
                elif s[i] == '(':
                    cur = str(recr(i+1, pair_index[i]-1))
                    if symbol == ' ':
                        ans += int(cur)
                    elif (cur[0] != '-' and symbol == '+') or (cur[0] == '-' and symbol == '-'):
                        ans += abs(int(cur))
                    else:
                        ans += -abs(int(cur))
                    
                    cur = '0'
                    symbol = ' '
                    i = pair_index[i]
                else:
                    cur += s[i]
                    
                i += 1
                
            ans += int(symbol + cur)
            return ans
        
        return recr(0, n-1)