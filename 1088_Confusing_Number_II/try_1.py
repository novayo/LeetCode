class Solution:
    def confusingNumberII(self, N: int) -> int:
        table = {
            99: 18,
            199: 40, 699: 62,899: 84,999: 106,
            1999: 226, 6999: 346,8999: 466,9999: 586,
            19999: 1196, 69999: 1806,89999: 2416,99999: 3026,
            199999: 6126, 699999: 9226,899999: 12326, 999999: 15426,
            1999999: 30976, 6999999: 46526, 8999999: 62076, 9999999: 77626,
            19999999: 155626, 69999999: 233626, 89999999: 311626, 99999999: 389626,
            199999999: 779876, 699999999: 1170126, 899999999: 1560376, 999999999: 1950626
        }
        tmp = str(N)
        n = 1 if N < 100 else int(tmp[0]) * (10**(len(tmp)-1))
        n = n if n-1 in table else 0
        ans = int(self.confusingNumber(N)) + (0 if n==0 else table[n-1])
        digit = 0
        pre = 0
        
        while n < N:
            n_str = str(n)
            digit = len(n_str)-1
            
            for i, s in enumerate(n_str):
                if n_str[i] == '2':
                    n += 4 * (10**(digit-i))
                    break
                elif n_str[i] == '7':
                    n += 1 * (10**(digit-i))
                    break
            if n >= N: break
            if self.confusingNumber(n):
                ans += 1
            n += 1
        return ans

        
    def confusingNumber(self, N: int) -> bool:
        dp = {'0':0,'1':1,'6':9,'8':8,'9':6}
        
        ans=0
        for i, s in enumerate(str(N)):
            if s in dp:
                ans += dp[s]*(10**i)
            else:
                return False
        
        return ans != N
