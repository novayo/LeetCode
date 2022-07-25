class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        '''
                                     i
        start = "XXXRXXLXXXXXXXXRXXXR"
        end =   "XXXXRLXXXXXXXXXXXXRR"
                                     j
        '''
        i = j = 0
        n = len(start)
        
        while i < n or j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            
            if i >= n and j >= n:
                return True
            elif i >= n or j >= n:
                return False
            else:
                if start[i] != end[j]:
                    return False
                elif start[i] == 'R' and i > j:
                    return False
                elif start[i] == 'L' and i < j:
                    return False
                else:
                    i, j = i+1, j+1
        
        return i >= n and j >= n
