class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        '''
        time complextity: O(n)
        we do one pass for counting the element in secret and guess => O(n)
        跑 0~9，如果兩邊都有出現，取最小值去累加 => O(n)
        之後再找有沒有相同的位置，一個B變成一個A => O(n)
        
        
        先假設沒有A，計算B
        之後再找有沒有相同的位置，一個B變成一個A
        
        secret = "1123", guess = "0111"
        1. 2B
        2. (0+1)A (2-1)B = 1A1B
        '''
        
        # 紀錄個別的個數 => dict
        d_secret = {}
        d_guess = {}
        
        ## O(n)
        for s in secret:
            if s not in d_secret:
                d_secret[s] = 0
            d_secret[s] += 1
        
        ## O(n)
        for g in guess:
            if g not in d_guess:
                d_guess[g] = 0
            d_guess[g] += 1
        
        
        # 跑 0~9，如果兩邊都有出現，取最小值去累加 => O(n)
        B = 0
        for i in range(0, 9+1):
            tmp = str(i)
            if tmp in d_secret and tmp in d_guess:
                count1 = d_secret[tmp]
                count2 = d_guess[tmp]
                
                B += min(count1, count2)
        
        # 之後再找有沒有相同的位置，一個B變成一個A => O(n)
        A = 0
        for i in range(len(guess)):
            target1 = secret[i]
            target2 = guess[i]
            
            if target1 == target2:
                A += 1
                B -= 1
        
        return '{}A{}B'.format(A, B)