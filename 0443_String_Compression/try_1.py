class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        one pointer -> replace
        one pointer -> loop for chars
        '''
        
        i = 0
        pre_char, number = '', 0
        for j, char in enumerate(chars):
            if pre_char == char:
                number += 1
            else:
                if number > 1:
                    for _s in str(number):
                        chars[i] = _s
                        i += 1
                chars[i] = char
                i += 1
                pre_char = char
                number = 1
        
        if number > 1:
            for _s in str(number):
                chars[i] = _s
                i += 1
        
        return i