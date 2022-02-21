class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        n = len(digits)
        table = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        def recr(i, cur_string):
            nonlocal ans
            
            if i >= n:
                ans.append(cur_string)
                return
            
            for digit in table[digits[i]]:
                recr(i+1, cur_string+digit)
        
        ans = []
        recr(0, '')
        return ans