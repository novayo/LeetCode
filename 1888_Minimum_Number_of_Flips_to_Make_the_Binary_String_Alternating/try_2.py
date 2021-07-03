class Solution:
    def minFlips(self, s: str) -> int:
        _1010, _0101 = 0, 0
        length = 0
        
        if len(s) % 2 == 0:
            # calculate 0~len(s)
            for i, _s in enumerate(s):
                if i % 2 == 0:
                    _1010 += 1 if _s == '1' else 0
                    _0101 += 1 if _s == '0' else 0
                else:
                    _1010 += 1 if _s == '0' else 0
                    _0101 += 1 if _s == '1' else 0
                length += 1
            return len(s) - max(_1010, _0101)
        else:
            # calculate 0~len(s)-1
            for i, _s in enumerate(s[:-1]):
                if i % 2 == 0:
                    _1010 += 1 if _s == '1' else 0
                    _0101 += 1 if _s == '0' else 0
                else:
                    _1010 += 1 if _s == '0' else 0
                    _0101 += 1 if _s == '1' else 0
                length += 1

            # define
            ans = float('inf')
            loop_s = s + s
            next_1010 = "1" if length % 2 == 0 else "0"
            next_0101 = "1" if length % 2 == 1 else "0"
            i, j = 0, length-1 # for _1010

            # loop
            for _ in range(len(s)):
                # consider i~j+1
                _1010 += 1 if loop_s[j+1] == next_1010 else 0
                _0101 += 1 if loop_s[j+1] == next_0101 else 0

                # check answer => consider i~j+1
                ans = min(ans, len(s) - max(_1010, _0101))

                # remove head
                _1010 += -1 if loop_s[i] == "1" else 0
                _0101 += -1 if loop_s[i] == "0" else 0

                # swap
                _1010, _0101 = _0101, _1010

                # sliding window
                i, j = i+1, j+1

            return ans
