class Solution:
    def countOfAtoms(self, formula: str) -> str:
        '''
        大寫 + 數字 / 小寫英文(多個) / 大寫
        數字只會 + 數字
        
        大寫、'(' ')' 是一個斷點
        '''
        
        index_parentheses = {}
        stack = []
        for i, s in enumerate(formula):
            if s == '(':
                stack.append(i)
            elif s == ')':
                index_parentheses[stack.pop()] = i
        
        def get_num(idx, j):
            num = ''
            while idx <= j:
                if formula[idx].isdigit():
                    num += formula[idx]
                    idx += 1
                else:
                    break
                    
            if num == '':
                return idx, 1
            return idx, int(num)
        
        def get_counter(i, j):
            ret = collections.Counter()
            
            if i == j:
                ret[formula[i]] += 1
                return ret
            
            idx = i
            while idx <= j:
                if formula[idx] == '(':
                    candidate = get_counter(idx+1, index_parentheses[idx]-1)
                    idx, num = get_num(index_parentheses[idx]+1, j)
                    
                    for w, c in candidate.items():
                        ret[w] += c * num
                else:
                    # uppercase
                    candidate = formula[idx]
                    idx += 1
                    while idx <= j:
                        if formula[idx].islower():
                            candidate += formula[idx]
                            idx += 1
                        else:
                            break
                    
                    idx, num = get_num(idx, j)
                    ret[candidate] += num
            return ret
        
        counter = get_counter(0, len(formula)-1)
        ans = []
        for w in sorted(counter.keys()):
            c = counter[w]
            if c == 1:
                ans.append(w)
            else:
                ans.append(w + str(c))
        
        return ''.join(ans)