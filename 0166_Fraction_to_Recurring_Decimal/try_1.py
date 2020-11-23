class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        '''
        要()的地方: 餘數 重複出現 的第一個位置~最後
        '''
        if numerator == 0:
            return "0"
        
        ans = []
        repeat = []
        offset = 0
        
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            offset = 1
            ans.append("-")
            
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        ans.append(str(numerator // denominator))
        numerator = numerator % denominator
        
        if numerator == 0:
            return ''.join(ans)
        
        ans.append('.')
        
        while numerator > 0:
            if numerator in repeat:
                index = repeat.index(numerator)
                ans.insert(index+2+offset, "(")
                ans.append(")")
                break
            
            repeat.append(numerator)
            numerator *= 10
            ans.append(str(numerator // denominator))
            numerator %= denominator

        return ''.join(ans)