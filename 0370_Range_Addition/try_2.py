class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # sweep line
        
        
        arr = [0] * length
        for start, end, inc in updates:
            arr[start] += inc
            
            if end + 1 < length:
                arr[end+1] -= inc
        
        cur = 0
        for i in range(length):
            cur += arr[i]
            arr[i] = cur
        return arr
