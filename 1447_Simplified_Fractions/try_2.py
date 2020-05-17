class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x    
        
        res = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if gcd(i, j) == 1:
                    res.append(str(j) + '/' + str(i))
        return res
