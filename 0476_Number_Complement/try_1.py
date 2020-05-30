class Solution:
    def findComplement(self, num: int) -> int:
        if num==0:
            return 1
        ans=0
        power=0
        while num>0:
            if num%2==0:
                ans+=2**power
            num//=2
            power+=1
        return ans
