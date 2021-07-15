class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0]*length
        for update in updates:
            start, end, inc = update
            ans[start] += inc
            
            if end < length-1:
                ans[end+1] -= inc
        
        for i in range(1, length):
            ans[i] += ans[i-1]
        return ans
