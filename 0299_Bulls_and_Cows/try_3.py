class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        '''
        掃過一遍secret、guess後取得幾A，跟其他個數
        
        union keys => 並指loop keys求最小 => 幾B累加
        '''
        
        A = B = 0
        n = len(secret)
        table_secret = collections.defaultdict(int)
        table_guess = collections.defaultdict(int)
        
        # get A
        for i in range(n):
            s = secret[i]
            g = guess[i]
            if s == g:
                A += 1
            else:
                table_secret[s] += 1
                table_guess[g] += 1
        
        # union keys
        union_keys = table_secret.keys() & table_guess.keys()
        
        # loop union_keys to get B
        for key in union_keys:
            B += min(table_secret[key], table_guess[key])
        
        return '{}A{}B'.format(A, B)