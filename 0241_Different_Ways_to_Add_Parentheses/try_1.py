class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        '''
        遇到符號 => recr 符號左邊 / 符號右邊，看計算完的值是多少，然後再 "左邊'+'右邊" 去計算所有結果
        '''
        memo = {}
        def dfs(string):
            nonlocal memo
            if string in memo:
                return memo[string]
            if string.isdigit():
                return [int(string)]
            
            ret = []
            for i, c in enumerate(string):
                if c in ['+', '-', '*']:
                    left_list = dfs(string[:i])
                    right_list = dfs(string[i+1:])
                    
                    for l in left_list:
                        for r in right_list:
                            ret.append(eval(str(l) + c + str(r)))
            
            memo[string] = ret
            return ret
        
        return dfs(expression)
                
