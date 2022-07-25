class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # O(1440*2) time / O(1440) space
        def getTimeStamp(time):
            tmp = time.split(':')
            return int(tmp[0]) * 60 + int(tmp[1])
        
        if len(timePoints) > 1440:
            return 0
        
        # bucket
        buckets = [False] * 1440
        for time in timePoints:
            minutes = getTimeStamp(time)
            
            if buckets[minutes] == True:
                return 0
            
            buckets[minutes] = True
            
        # two pointer
        ans = float('inf')
        
        # find first True
        i = 0
        while i < 1440 and buckets[i] == False:
            i += 1
        
        for j in range(i+1, 2*1440):
            if buckets[j%1440] == True:
                ans = min(ans, j-i)
                i = j
        return ans
