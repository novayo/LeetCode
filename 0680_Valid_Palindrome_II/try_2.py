class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n-1
        
        while i < j and s[i] == s[j]:
            i, j = i+1, j-1
        
        if i >= j:
            return True
        
        # try to move left
        _i, _j = i+1, j
        while _i < _j and s[_i] == s[_j]:
            _i, _j = _i+1, _j-1
        
        if _i >= _j:
            return True
        
        # try to move right
        _i, _j = i, j-1
        while _i < _j and s[_i] == s[_j]:
            _i, _j = _i+1, _j-1
        
        if _i >= _j:
            return True
        
        return False
