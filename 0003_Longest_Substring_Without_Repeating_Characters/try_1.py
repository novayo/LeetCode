class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _str, l = "", 0
        for i in s:
            if i in _str:
                _str = "" if _str.index(i) == len(_str)-1 else _str[_str.index(i)+1:]
            _str += i
            l = len(_str) if len(_str) > l else l
        return l
