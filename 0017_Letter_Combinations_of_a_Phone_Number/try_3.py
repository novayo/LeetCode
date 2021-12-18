class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        table = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        
        ans = [""]
        
        for i in range(len(digits)-1, -1, -1):
            digit = int(digits[i])
            
            tmp = []
            for d in table[digit]:
                for j in range(len(ans)):
                    tmp.append(d + ans[j])
            ans = tmp
        
        return ans if ans != [""] else []
