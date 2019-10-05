class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        _dict = {}
        for value in arr:
            if value in _dict:
                _dict[value] += 1
            else:
                _dict[value] = 0
        
        _set = set()
        for value in _dict.values():
            if value in _set:
                return False
            else:
                _set.add(value)
        
        return True
