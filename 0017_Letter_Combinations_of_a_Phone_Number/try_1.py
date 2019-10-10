class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        _dict = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"],
                 "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}
        ans = collections.deque()
        
        def dfs(string: str, n: int):
            if n>len(digits)-1:
                return
            for value in _dict[digits[n]]:
                dfs(string+value, n+1)
                if len(string+value) == len(digits):
                    ans.append(string+value)
                
        dfs("", 0)
        return ans
