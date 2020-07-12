class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        紀錄找到的質數，並用質數去判斷是否target為質數
        '''
        
        ans = 0
        
        dp = []
        def isPrimes(target):
            mid = sqrt(target)
            
            if mid - int(mid) == 0:
                return False
            
            for i in dp:
                if i > mid:
                    break
                if target % i == 0:
                    return False
            dp.append(target)
            return True
                    
        
        for i in range(2, n):
            if isPrimes(i):
                ans += 1
        return ans
