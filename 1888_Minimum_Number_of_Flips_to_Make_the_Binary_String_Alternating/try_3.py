class Solution:
    def minFlips(self, s: str) -> int:
        def compare(pattern):
            ret = 0
            for OE, d in ans_patten.items():
                for _01, require in d.items():
                    if require > pattern[OE][_01]:
                        ret += require - pattern[OE][_01]
            return ret
        
        ODD, EVEN = 0, 1
        s_len = len(s)
        
        ans_patten = {
            ODD: {
                0: s_len // 2,
                1: 0
            }, 
            EVEN: {
                0: 0,
                1: ceil(s_len / 2)
            }
        }
        
        # build pattern
        pattern = {
            ODD: {0:0, 1:0}, 
            EVEN: {0:0, 1:0}
        }
        for i, _s in enumerate(s):
            if i % 2 == 0:
                if _s == '0':
                    pattern[EVEN][0] += 1
                else:
                    pattern[EVEN][1] += 1
            else:
                if _s == '0':
                    pattern[ODD][0] += 1
                else:
                    pattern[ODD][1] += 1
        
        ans = float('inf')
        for i in range(s_len):
            # swap
            pattern[EVEN][1], pattern[ODD][1] = pattern[ODD][1], pattern[EVEN][1]
            pattern[EVEN][0], pattern[ODD][0] = pattern[ODD][0], pattern[EVEN][0]
            
            if s_len % 2 == 1:
                if s[i] == '0':
                    pattern[EVEN][0] += 1
                    pattern[ODD][0] -= 1
                else:
                    pattern[EVEN][1] += 1
                    pattern[ODD][1] -= 1
            
            if s_len % 2 == 0 and i == 2:
                break
            
            # compare
            ret = compare(pattern)
            ans = min(ans, ret, s_len - ret)
        return ans