class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
#         ans = 0

#         O(n^2)
#         for j in J:
#             # search
#             for s in S:
#                 if j == s:
#                     ans += 1
#         return ans
        
        
        ''''''
        
        S_dict = {}
        
        # preprocess => count stones => O(n)
        for s in S:
            if s not in S_dict:
                S_dict[s] = 0
            S_dict[s] += 1
        
        # {'a': 1, 'A': 2, 'b': 4}
        print(S_dict)
        
        # loop => O(n)
        ans = 0
        for j in J:
            if j in S_dict:
                number = S_dict[j]
                ans += number
        
        return ans