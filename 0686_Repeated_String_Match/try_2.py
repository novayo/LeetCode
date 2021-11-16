class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a == b or b in a:
            return 1
        else:
            split_list = b.split(a)
            
            if len(split_list) == 1:
                if b in a+a:
                    return 2
                else:
                    return -1
            else:
                for s in split_list[1:-1]:
                    if s != '':
                        return -1
                
                prefix, postfix = split_list[0], split_list[-1]
                ans = (len(b) - len(prefix) - len(postfix)) // len(a)
                
                if prefix != '':
                    ans += 1
                    _a, _prefix = len(a)-1, len(prefix)-1
                    while _a >= 0 and _prefix >= 0:
                        if a[_a] == b[_prefix]:
                            _a, _prefix = _a-1, _prefix-1
                        else:
                            return -1
                
                if postfix != '':
                    ans += 1
                    _a, _postfix = 0, 0
                    while _a < len(a) and _postfix < len(postfix):
                        if a[_a] == postfix[_postfix]:
                            _a, _postfix = _a+1, _postfix+1
                        else:
                            return -1
                return ans
