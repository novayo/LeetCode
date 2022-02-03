class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def char2int(char):
            return ord(char) - ord('0')
        
        def add(string1, string2):
            ans = ''
            carry = 0
            i, j = len(string1)-1, len(string2)-1
            
            while i >= 0 or j >= 0 or carry > 0:
                if i >= 0:
                    carry += char2int(string1[i])
                    i -= 1
                if j >= 0:
                    carry += char2int(string2[j])
                    j -= 1
                
                ans = str(carry%10) + ans
                carry //= 10
            
            return ans
        
        def mul(string1, char2):
            _m = char2int(char2)
            ans = ''
            carry = 0
            for s in string1[::-1]:
                _s = char2int(s)
                
                a = _m * _s + carry
                ans = str(a%10) + ans
                carry = a // 10
            
            if carry:
                ans = str(carry) + ans
            
            return ans
        
        ans = '0'
        for i2, n2 in enumerate(num2[::-1]):
            mul_ret = mul(num1, n2)
            if mul_ret[0] != '0':
                ans = add(ans, mul_ret + '0'*i2)
        return ans
