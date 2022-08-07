class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        i = j = 0
        
        while True:
            while i < n and start[i] == 'X':
                i += 1
            
            while j < n and end[j] == 'X':
                j += 1
            
            if i >= n and j >= n:
                return True
            elif i >= n or j >= n:
                return False
            
            if start[i] != end[j]:
                return False
            elif start[i] == 'L' and i < j:
                return False
            elif start[i] == 'R' and i > j:
                return False
            else:
                i, j = i+1, j+1
        
        return -1
