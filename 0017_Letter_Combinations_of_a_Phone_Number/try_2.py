class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        table = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
                "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        def recr(index, string):
            if index == len(digits):
                ans.append(string)
                return
            
            for digit in table[digits[index]]:
                recr(index+1, string + digit)
        
        ans = []
        recr(0, "")
        return ans