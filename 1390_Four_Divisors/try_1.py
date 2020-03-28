class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        
        for n in nums:
            tmp = 2
            tmps = n+1
            
            a = n**(1/2)
            if floor(a) == ceil(a):
                continue
            else:
                a = int(a)+1
            
            flag = False
            for i in range(2, a):
                if n % i == 0:
                    tmp += 2
                    tmps += i
                    tmps += n//i
                
                if tmp > 4:
                    flag = True
                    break
            
            # print(tmp, tmps)
            if flag == False and tmp == 4:
                ans += tmps
        
        return ans
