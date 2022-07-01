class Solution:
    def evaluate(self, expression: str) -> int:
        def getTwoElements(s, e, localValue={}):
            # last element
            if ' ' not in expression[s:e+1]:
                if expression[s] == '(':
                    return recr(s+1, pair_indices[s]-1, localValue), None, e+1
                else:
                    return localValue.get(expression[s:e+1], [expression[s:e+1]])[-1], None, e+1
            
            a = b = None
            tmp = ''
            i = s
            while i <= e and (a == None or b == None):
                if expression[i] == '(':
                    if not a:
                        a = recr(i+1, pair_indices[i]-1, localValue)
                    else:
                        b = recr(i+1, pair_indices[i]-1, localValue)
                    i = pair_indices[i]+1 # on space
                elif expression[i] != ' ':
                    tmp += expression[i]
                else:
                    if not a:
                        a = tmp
                    else:
                        b = tmp
                    tmp = ''
                i += 1
            
            # last element
            if tmp:
                b = tmp
            
            return a, b, i
        
        def recr(s, e, localValue):
            # get operation
            op = ''
            for exp in expression[s: e+1]:
                if exp == ' ':
                    break
                op += exp
            
            if op == 'add':
                s += 4 # skip "add "
                a, b, _ = getTwoElements(s, e, localValue)
                return str(int(localValue.get(a, [a])[-1]) + int(localValue.get(b, [b])[-1]))
            elif op == 'mult':
                s += 5 # skip "mult "
                a, b, _ = getTwoElements(s, e, localValue)
                return str(int(localValue.get(a, [a])[-1]) * int(localValue.get(b, [b])[-1]))
            else:
                s += 4 # skip "let "
                stack = []
                while s <= e:
                    a, b, s = getTwoElements(s, e, localValue)
                    
                    if b == None:
                        ret = localValue.get(a, [a])[-1]
                        for s in stack:
                            localValue[s].pop()
                        return ret
                    
                    if a not in localValue:
                        localValue[a] = []
                    stack.append(a)
                    localValue[a].append(localValue.get(b, [b])[-1])
        
        pair_indices = self.getPair(expression)
        return recr(1, len(expression)-2, {})
        
    def getPair(self, expression):
        pair = {}
        stack = []
        for i, e in enumerate(expression):
            if e == '(':
                stack.append(i)
            elif e == ')':
                pair[stack.pop()] = i
        return pair

