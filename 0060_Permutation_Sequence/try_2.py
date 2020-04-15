class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = ""
        found = set()
        
        tmpn = n
        while tmpn>0:
            # permutationLen = 總長度 （1*2*...n
            # setLen = 每個數字的長度
            permutationLen = 1
            for i in range(1, tmpn+1):
                permutationLen *= i
            setLen = permutationLen // tmpn
            
            # i是哪個數字（假設是2
            # k是第幾個2
            for i in range(1, n+1):
                if i in found:
                    continue
                
                if k-setLen <= 0:
                    found.add(i)
                    ans += str(i)
                    break
                k -= setLen
            tmpn -= 1

        return ans
