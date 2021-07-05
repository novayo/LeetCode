class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # 紀錄前面可以放誰
        MODULE = 10**9 + 7
        table = {
            '' : ['a', 'e', 'i', 'o', 'u'],
            'a': ['e', 'i', 'u'],
            'e': ['a', 'i'],
            'i': ['e', 'o'],
            'o': ['i'],
            'u': ['i', 'o']
        }
        
        def recr(n, cur, memo={}):
            if n == 0:
                return 1
            
            if (n, cur) in memo:
                return memo[n, cur]
            
            ans = 0
            for s in table[cur]:
                ans += (recr(n-1, s, memo)) % MODULE
            memo[n, cur] = ans % MODULE
            return memo[n, cur]

        return recr(n, '')
