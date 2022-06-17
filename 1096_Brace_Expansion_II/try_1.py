class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def multiply(set1, set2):
            ret = set()
            for s1 in set1:
                for s2 in set2:
                    ret.add(s1 + s2)
            return ret
        
        # get index
        indices = {}
        stack = []
        for i, exp in enumerate(expression):
            if exp == '{':
                stack.append(i)
            elif exp == '}':
                indices[stack.pop()] = i
        
        # recr
        memo = {}
        def recr(start, end):
            if expression[start: end+1] in memo:
                return memo[expression[start: end+1]]
            
            next_word = True
            stack = []
            i = start
            while i <= end:
                if expression[i] == ',':
                    next_word = True
                    i += 1
                    continue
                elif expression[i] == '{':
                    ret = recr(i+1, indices[i]-1)
                    if next_word:
                        stack.append(ret)
                    else:
                        stack[-1] = multiply(stack[-1], ret)
                    i = indices[i] + 1
                else:
                    if next_word:
                        stack.append({expression[i]})
                    else:
                        stack[-1] = multiply(stack[-1], {expression[i]})
                    i += 1
                next_word = False

            # get answer
            ret = set()
            for element in stack:
                ret |= element
                
            memo[expression[start: end+1]] = ret
            return ret
        
        return sorted(recr(0, len(expression)-1))