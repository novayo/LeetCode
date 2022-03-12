class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        for i in range(1, len(num)):
            a = num[:i]
            if int(a) != 0 and a[0] == '0':
                continue
            
            for j in range(i+1, len(num)):
                _a = a
                b = num[i:j]
                if int(b) != 0 and b[0] == '0':
                    continue
                
                attempt = str(int(_a) + int(b))
                k = j + len(attempt)
                while num[j:k] == attempt:
                    
                    if k > len(num):
                        break
                    elif k == len(num):
                        return True
                            
                    _a, b = b, attempt
                    attempt = str(int(_a) + int(b))
                    j = k
                    k = j + len(attempt)
        
        return False

