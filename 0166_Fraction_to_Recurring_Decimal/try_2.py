class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        
        ans = ''
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            ans += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        ans += str(numerator // denominator)
        rest = numerator % denominator
        if rest == 0:
            return ans
        
        ans += '.'
        
        found = set([rest])
        
        # find first hit
        tmp = ''
        while rest > 0:
            rest *= 10
            while rest < denominator:
                tmp += '0'
                rest *= 10
            tmp += str(rest // denominator)
            rest %= denominator
            
            if rest in found:
                break
            else:
                found.add(rest)
        
        if rest == 0:
            return ans + tmp
        
        # if first hit => find ()
        tmp2 = ''
        found = set()
        while rest not in found:
            found.add(rest)
            rest *= 10
            while rest < denominator:
                tmp2 += '0'
                rest *= 10
            tmp2 += str(rest // denominator)
            rest %= denominator
        
        return ans + tmp[:-len(tmp2)] + '(' + tmp2 + ')'