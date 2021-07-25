class Solution:
    def findIntegers(self, n: int) -> int:
        # 2, 3, 5, 8
        bit = bin(n+1)[2:]
        
        dp = [1, 2]
        for i in range(2, len(bit)):
            dp.append(dp[i-2] + dp[i-1])
        
        ans = 0
        for i in range(len(bit)):
            if bit[i] == '0': 
                continue
            ans += dp[~i] # 因為dp只紀錄1的數量
            
            # 不要連續的1
            if i > 0 and bit[i-1] == '1':
                break
        return ans
