class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # 三進位，若有位元為2，代表不能轉換成3 （因為不能有重複的x）
        
        while n:
            if n % 3 == 2:
                return False
            n //= 3
        
        return True
