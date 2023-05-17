class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        table = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y','z']}
        
        ans = []
        def backtracking(idx, curString):
            nonlocal ans
            if idx >= len(digits):
                ans.append(curString)
                return
            
            for s in table[digits[idx]]:
                backtracking(idx+1, curString + s)
        
        backtracking(0, "")
        return ans
