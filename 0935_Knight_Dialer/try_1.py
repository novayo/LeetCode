class Solution:
    def knightDialer(self, n: int) -> int:
        
        '''
        start from 10 number
            -> each stage => at different number & n (we can memo the count)
            
            memo => 從8開始走，剩兩步時，走到1 => 2步 => 從8走，能走2步 + 2步
            
        '''
        if n == 1:
            return 10
        
        MOD = 10**9 + 7
        
        validJump = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        
        memo = {}
        
        def dfs(n, number):
            jumps = 0
            
            if n == 0:
                return 1
            
            if (n, number) in memo:
                return memo[n, number]
            
            for num in validJump[number]:
                jumps = (jumps + dfs(n-1, num)) % MOD
            
            memo[n, number] = jumps
            return memo[n, number]
          
        ans = 0
        for number in range(10):
            if number == 5:
                continue
            ans = (ans + dfs(n-1, number)) % MOD
        
        return ans % MOD
