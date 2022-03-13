class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        isPrime = [True] * n
        
        # init
        isPrime[0] = isPrime[1] = False
    
        # get prime
        for i in range(2, int(sqrt(n))+1):
            if isPrime[i] == True:
                index = i*i
                while index < n:
                    isPrime[index] = False
                    index += i

        # count ans
        return sum(isPrime)