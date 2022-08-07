class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = 60 * 24
        
        if len(timePoints) > n:
            return 0
        
        arr = [0] * n
        
        for time in timePoints:
            m, s = time.split(':')
            timestamp = int(m)*60 + int(s)
            arr[timestamp] += 1
            if arr[timestamp] > 1:
                return 0
        
        # find first 1
        i = 0
        while i < n and arr[i] == 0:
            i += 1
        
        ans = float('inf')
        for j in range(i+1, n * 2):
            if arr[j%n] == 1:
                ans = min(ans, j-i)
                i = j
        return ans
