class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if len(a) > len(b):
            if b in a:
                return 1
            elif b in a+a:
                return 2
            else:
                return -1
        elif len(a) == len(b):
            if b in a:
                return 1
            elif b in a+a:
                return 2
            else:
                return -1
        else:
            ans = 0
            
            split_b = b.split(a)
            
            if len(split_b) == 1:
                if b in a+a:
                    return 2
                else:
                    return -1
            
            length = 0
            for i in range(len(split_b)):
                length += len(split_b[i])
                if i > 0 and i < len(split_b)-1 and split_b[i] != '':
                    return -1
            ans += (len(b) - length) // len(a)
            
            # prefix
            prefix = split_b[0]
            if prefix != '':
                ans += 1
            _b = len(prefix) - 1
            _a = len(a) - 1
            while _b >= 0 and _a >= 0:
                if a[_a] != prefix[_b]:
                    break
                _a -= 1
                _b -= 1
            
            if _b >= 0:
                return -1
            
            # postfix
            postfix = split_b[-1]
            if postfix != '':
                ans += 1
            _b = 0
            _a = 0
            while _b < len(postfix) and _a < len(a):
                if a[_a] != postfix[_b]:
                    break
                _a += 1
                _b += 1
            
            if _b < len(postfix):
                return -1
            
            return ans
            
        
